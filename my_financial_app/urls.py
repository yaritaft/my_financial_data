from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListTodoView.as_view()),
    path("<int:pk>/", views.DetailTodoView.as_view()),
    path("create/", views.CreateTodoView.as_view(), name="todo_create"),
]
