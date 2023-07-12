from django.urls import path
from .views import *

urlpatterns = [
    path('task/<int:id>/', TaskDetailModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('tasks/', TaskModelViewSet.as_view({
        "get": 'list'
    })),

]
