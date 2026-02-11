from djongo import models


class User(models.Model):
    """User profile model"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=255)
    age = models.IntegerField()
    fitness_level = models.CharField(max_length=50)
    total_points = models.IntegerField(default=0)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Team(models.Model):
    """Team model"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.JSONField(default=list)
    total_points = models.IntegerField(default=0)
    created_at = models.CharField(max_length=100)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teams'


class Activity(models.Model):
    """Activity log model"""
    user_email = models.EmailField()
    user_name = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    date = models.CharField(max_length=100)
    distance_km = models.FloatField(null=True, blank=True)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.user_name} - {self.activity_type}"

    class Meta:
        db_table = 'activities'


class Leaderboard(models.Model):
    """Leaderboard model"""
    rank = models.IntegerField()
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    team = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField()
    activities_count = models.IntegerField()
    total_calories_burned = models.IntegerField(default=0)
    updated_at = models.CharField(max_length=100)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.rank}. {self.user_name}"

    class Meta:
        db_table = 'leaderboard'


class Workout(models.Model):
    """Workout suggestion model"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration_minutes = models.IntegerField()
    difficulty_level = models.CharField(max_length=50)
    exercises = models.JSONField(default=list)
    target_audience = models.CharField(max_length=255)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workouts'
