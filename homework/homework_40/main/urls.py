from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('tasklist', views.tasklist, name='tasklist'),
    path('taskcreate', views.taskcreate, name='taskcreate'),
    path('postlist', views.postlist, name='postlist'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
