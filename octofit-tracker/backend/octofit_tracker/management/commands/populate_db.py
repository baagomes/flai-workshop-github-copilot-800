from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Delete existing data to allow re-population
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Sample superheroes and teams
        marvel_heroes = [
            {
                'name': 'Tony Stark',
                'email': 'tony.stark@marvel.com',
                'team': 'Team Marvel',
                'age': 45,
                'fitness_level': 'Advanced',
                'total_points': 2500
            },
            {
                'name': 'Steve Rogers',
                'email': 'steve.rogers@marvel.com',
                'team': 'Team Marvel',
                'age': 100,
                'fitness_level': 'Expert',
                'total_points': 3500
            },
            {
                'name': 'Bruce Banner',
                'email': 'bruce.banner@marvel.com',
                'team': 'Team Marvel',
                'age': 40,
                'fitness_level': 'Intermediate',
                'total_points': 2000
            },
            {
                'name': 'Natasha Romanoff',
                'email': 'natasha.romanoff@marvel.com',
                'team': 'Team Marvel',
                'age': 35,
                'fitness_level': 'Expert',
                'total_points': 3000
            },
        ]

        dc_heroes = [
            {
                'name': 'Clark Kent',
                'email': 'clark.kent@dc.com',
                'team': 'Team DC',
                'age': 35,
                'fitness_level': 'Expert',
                'total_points': 3200
            },
            {
                'name': 'Bruce Wayne',
                'email': 'bruce.wayne@dc.com',
                'team': 'Team DC',
                'age': 40,
                'fitness_level': 'Advanced',
                'total_points': 2800
            },
            {
                'name': 'Diana Prince',
                'email': 'diana.prince@dc.com',
                'team': 'Team DC',
                'age': 30,
                'fitness_level': 'Expert',
                'total_points': 3400
            },
            {
                'name': 'Barry Allen',
                'email': 'barry.allen@dc.com',
                'team': 'Team DC',
                'age': 30,
                'fitness_level': 'Advanced',
                'total_points': 2600
            },
        ]

        # Insert users
        all_users = marvel_heroes + dc_heroes
        db.users.insert_many(all_users)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(all_users)} users'))

        # Create Teams
        teams = [
            {
                'name': 'Team Marvel',
                'description': 'Marvel Universe Team',
                'members': [u['email'] for u in marvel_heroes],
                'total_points': sum(u['total_points'] for u in marvel_heroes),
                'created_at': '2025-01-01'
            },
            {
                'name': 'Team DC',
                'description': 'DC Universe Team',
                'members': [u['email'] for u in dc_heroes],
                'total_points': sum(u['total_points'] for u in dc_heroes),
                'created_at': '2025-01-01'
            },
        ]
        db.teams.insert_many(teams)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(teams)} teams'))

        # Create Activities
        activities = []
        activity_types = ['Running', 'Weightlifting', 'Yoga', 'Swimming', 'Cycling']
        for i, user in enumerate(all_users):
            for j, activity_type in enumerate(activity_types):
                activities.append({
                    'user_email': user['email'],
                    'user_name': user['name'],
                    'activity_type': activity_type,
                    'duration_minutes': 30 + (j * 10),
                    'calories_burned': 200 + (j * 50),
                    'date': f'2025-02-{(i % 10) + 1:02d}',
                    'distance_km': 5.0 + (j * 0.5) if activity_type in ['Running', 'Cycling'] else None,
                })
        db.activities.insert_many(activities)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(activities)} activities'))

        # Create Leaderboard
        leaderboard = []
        for rank, user in enumerate(sorted(all_users, key=lambda x: x['total_points'], reverse=True), 1):
            # Calculate total calories burned for this user
            user_calories = sum(a['calories_burned'] for a in activities if a['user_email'] == user['email'])
            leaderboard.append({
                'rank': rank,
                'user_name': user['name'],
                'user_email': user['email'],
                'team': user['team'],
                'team_name': user['team'],
                'points': user['total_points'],
                'activities_count': len([a for a in activities if a['user_email'] == user['email']]),
                'total_calories_burned': user_calories,
                'updated_at': '2025-02-11'
            })
        db.leaderboard.insert_many(leaderboard)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(leaderboard)} leaderboard entries'))

        # Create Workouts
        workouts = [
            {
                'name': 'Morning Run',
                'description': 'Begin your day with an energizing 5K run',
                'duration_minutes': 30,
                'difficulty_level': 'Intermediate',
                'exercises': ['Warm-up jog', 'Main 5K run', 'Cool-down walk'],
                'target_audience': 'All fitness levels'
            },
            {
                'name': 'Strength Training',
                'description': 'Build muscle with compound weightlifting exercises',
                'duration_minutes': 60,
                'difficulty_level': 'Advanced',
                'exercises': ['Squats', 'Bench Press', 'Deadlifts'],
                'target_audience': 'Intermediate to Advanced'
            },
            {
                'name': 'Yoga Flow',
                'description': 'Improve flexibility and balance',
                'duration_minutes': 45,
                'difficulty_level': 'Beginner',
                'exercises': ['Warm-up', 'Sun Salutation', 'Standing poses', 'Savasana'],
                'target_audience': 'All fitness levels'
            },
            {
                'name': 'HIIT Workout',
                'description': 'High-intensity interval training for maximum calorie burn',
                'duration_minutes': 30,
                'difficulty_level': 'Advanced',
                'exercises': ['Burpees', 'Mountain Climbers', 'Jump Squats', 'Push-ups'],
                'target_audience': 'Advanced'
            },
            {
                'name': 'Swimming Session',
                'description': 'Low-impact full-body cardio workout',
                'duration_minutes': 45,
                'difficulty_level': 'Intermediate',
                'exercises': ['Freestyle', 'Backstroke', 'Breaststroke', 'Cool-down'],
                'target_audience': 'All fitness levels'
            }
        ]
        db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(workouts)} workouts'))

        # Create unique index on email field for users
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('✓ Created unique index on email field'))

        self.stdout.write(self.style.SUCCESS('\n✅ Database population completed successfully!'))
