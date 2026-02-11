from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer


@api_view(['GET'])
def api_root(request):
    """API root endpoint"""
    return Response({
        'users': reverse('user-list', request=request),
        'teams': reverse('team-list', request=request),
        'activities': reverse('activity-list', request=request),
        'leaderboard': reverse('leaderboard-list', request=request),
        'workouts': reverse('workout-list', request=request),
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model
    Provides CRUD operations for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Team model
    Provides CRUD operations for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Activity model
    Provides CRUD operations for activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Leaderboard model
    Provides read-only operations for leaderboard
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Workout model
    Provides CRUD operations for workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
