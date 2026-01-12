from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.teams.views import TeamViewSet
from api.tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('api.users.urls', namespace='users')),
]