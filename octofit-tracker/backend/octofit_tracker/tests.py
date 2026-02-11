from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team='Test Team',
            age=30,
            fitness_level='Intermediate',
            total_points=1000
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
    
    def test_user_str(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'Test User')


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        """Set up test data"""
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
            members=['user1@example.com', 'user2@example.com'],
            total_points=5000,
            created_at='2025-01-01'
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(len(self.team.members), 2)


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        """Set up test data"""
        self.activity = Activity.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            activity_type='Running',
            duration_minutes=30,
            calories_burned=300,
            date='2025-02-11',
            distance_km=5.0
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.calories_burned, 300)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        """Set up test data"""
        self.workout = Workout.objects.create(
            name='Morning Run',
            description='A refreshing morning run',
            duration_minutes=30,
            difficulty_level='Intermediate',
            exercises=['Warm-up', 'Main run', 'Cool-down'],
            target_audience='All fitness levels'
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Morning Run')
        self.assertEqual(self.workout.difficulty_level, 'Intermediate')


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create(
            name='API Test User',
            email='apitest@example.com',
            team='API Test Team',
            age=25,
            fitness_level='Beginner',
            total_points=500
        )
    
    def test_get_users_list(self):
        """Test retrieving list of users"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        """Test creating a new user"""
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'team': 'New Team',
            'age': 28,
            'fitness_level': 'Advanced',
            'total_points': 1500
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""
    
    def test_api_root(self):
        """Test API root endpoint returns links to all endpoints"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
