from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'age', 'fitness_level', 'total_points']
        extra_kwargs = {
            'email': {'validators': []},  # Remove unique validator for bulk operations
        }

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if instance.pk:
            representation['id'] = str(instance.pk)
        return representation


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    members_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'members_count', 'total_points', 'created_at']

    def get_members_count(self, obj):
        """Get the count of members in the team"""
        if isinstance(obj.members, list):
            return len(obj.members)
        return 0

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if instance.pk:
            representation['id'] = str(instance.pk)
        return representation


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'user_name', 'activity_type', 'duration_minutes', 'calories_burned', 'date', 'distance_km']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if instance.pk:
            representation['id'] = str(instance.pk)
        return representation


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'rank', 'user_name', 'user_email', 'team', 'team_name', 'points', 'activities_count', 'total_calories_burned', 'updated_at']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if instance.pk:
            representation['id'] = str(instance.pk)
        return representation


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration_minutes', 'difficulty_level', 'exercises', 'target_audience']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if instance.pk:
            representation['id'] = str(instance.pk)
        return representation

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if instance.id:
            representation['id'] = str(instance.id)
        return representation
