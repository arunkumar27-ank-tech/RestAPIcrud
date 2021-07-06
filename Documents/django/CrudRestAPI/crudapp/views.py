from django.shortcuts import render
from rest_framework import serializers
from crudapp.models import Todo
from crudapp.serializers import Todoserializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def read(request):
    var1 = Todo.objects.all()
    serializer = Todoserializer(var1, many=True)
    return JsonResponse(serializer.data, safe = False)


@api_view(['GET'])
def view(request, pk):
    var1 = Todo.objects.get(id=pk)
    serializer = Todoserializer(var1, many=False)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def create(request):
    serializer = Todoserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def Update(request, pk):
    var1 = Todo.objects.get(id=pk)
    serializer = Todoserializer(instance=var1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)

@api_view(['DELETE'])
def abort(request,pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return Response('ITEM SUCCESSFULLY DELETED')