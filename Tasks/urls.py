from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('tasks', views.Task_List.as_view()),
    path('task/<int:id>', views.Task_Detail.as_view()),

    # path('/tasks', views.),
]
 