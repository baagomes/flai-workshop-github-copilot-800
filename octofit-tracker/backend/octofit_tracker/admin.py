from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['name', 'email', 'team', 'fitness_level', 'total_points']
    search_fields = ['name', 'email', 'team']
    list_filter = ['fitness_level', 'team']
    ordering = ['-total_points']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['name', 'total_points', 'created_at']
    search_fields = ['name']
    ordering = ['-total_points']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['user_name', 'activity_type', 'date', 'duration_minutes', 'calories_burned']
    search_fields = ['user_name', 'user_email', 'activity_type']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['rank', 'user_name', 'team', 'points', 'activities_count']
    search_fields = ['user_name', 'user_email', 'team']
    list_filter = ['team']
    ordering = ['rank']
    readonly_fields = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['name', 'difficulty_level', 'duration_minutes', 'target_audience']
    search_fields = ['name', 'description']
    list_filter = ['difficulty_level']
    ordering = ['name']
