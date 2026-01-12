from rest_framework import serializers
from .models import Task
from api.teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'creator', 'members', 'created_at']
        read_only_fields = ['creator']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' #