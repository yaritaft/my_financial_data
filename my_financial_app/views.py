from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ListTodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoView(generics.CreateAPIView):
    serializer_class = TodoSerializer


@api_view(["POST"])
def create_todo(request):
    serializer = TodoSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"})
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data)
