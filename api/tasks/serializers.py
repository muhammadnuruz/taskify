from rest_framework import serializers
from .models import Task
from api.teams.models import Team


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        team = data.get('team')
        assignee = data.get('assignee')

        if team:
            if assignee and not team.members.filter(id=assignee.id).exists():
                raise serializers.ValidationError({
                    'assignee': 'Faqat jamoa a\'zolariga vazifa biriktirish mumkin.'
                })

        return data