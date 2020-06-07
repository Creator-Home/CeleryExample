from django.urls import path,include
from example import views

urlpatterns = [
    path('', views.task_state, name='Task'),
    path('result', views.redisResult, name='TaskResult'),
]
