from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers,EmployeSerializers
from .models import Task,Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers


class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers

class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers

class EmployeeDetail(APIView):
    def get(self,request):
        obj = Employee.objects.all()
        serializer = EmployeSerializers(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = EmployeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeInfo(APIView):
    def get(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeSerializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg':'not found error'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeSerializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg':'not found error'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeSerializers(obj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg':'not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({'msg':'deleted'}, status=status.HTTP_204_NO_CONTENT)