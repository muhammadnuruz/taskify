from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team
from api.users.serializers import UserSerializer

User = get_user_model()


class TeamSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    members_count = serializers.IntegerField(source='members.count', read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'creator', 'members', 'members_count', 'created_at']


class MemberManageSerializer(serializers.Serializer):
    ACTION_CHOICES = (
        ('add', 'Qo\'shish'),
        ('remove', 'O\'chirish'),
    )
    action = serializers.ChoiceField(choices=ACTION_CHOICES, help_text="Amal turi: 'add' yoki 'remove'")
    email = serializers.EmailField(help_text="Jamoaga qo'shiladigan/o'chiriladigan foydalanuvchi emaili")

    class Meta:
        ref_name = 'MemberManage'