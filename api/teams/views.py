from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Team
from .serializers import TeamSerializer

User = get_user_model()


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Team.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        team = serializer.save(creator=self.request.user)
        team.members.add(self.request.user)

    @action(detail=True, methods=['post'], url_path='manage-members')
    def manage_members(self, request, pk=None):
        team = self.get_object()
        if team.creator != request.user:
            return Response({'error': 'Ruxsat berilmagan'}, status=status.HTTP_403_FORBIDDEN)

        action_type = request.data.get('action')
        email = request.data.get('email')

        try:
            target_user = User.objects.get(email=email, is_active=True)
            if action_type == 'add':
                team.members.add(target_user)
                return Response({'status': 'A\'zo qo\'shildi'})
            elif action_type == 'remove':
                if target_user == team.creator:
                    return Response({'error': 'Yaratuvchini o\'chirib bo\'lmaydi'}, status=400)
                team.members.remove(target_user)
                return Response({'status': 'A\'zo chetlatildi'})
        except User.DoesNotExist:
            return Response({'error': 'Foydalanuvchi topilmadi'}, status=404)
