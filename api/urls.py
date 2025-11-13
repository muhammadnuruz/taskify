from django.urls import path, include

urlpatterns = [
    path('users/', include("api.users.urls", namespace='users')),
    path('tasks/', include("api.tasks.urls", namespace='tasks')),
]
