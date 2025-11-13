from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assignee=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object_or_none(kwargs.get('pk'))
        if not task:
            return Response({'detail': 'This task does not exist.'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        task = self.get_object_or_none(kwargs.get('pk'))
        if not task:
            return Response({'detail': 'This task does not exist.'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object_or_none(kwargs.get('pk'))
        if not task:
            return Response({'detail': 'This task does not exist.'},
                            status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object_or_none(self, pk):
        try:
            return Task.objects.get(id=pk, assignee=self.request.user)
        except Task.DoesNotExist:
            return None
