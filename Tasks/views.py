from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TaskSerializer,AllTaskSerializer
# Create your views here.
def index(request):

    return render(request,"index.html")

class Task_List(APIView):
    def get(self,request):
      queryset=Task.objects.all()
      serializer=AllTaskSerializer(queryset,many=True)
      return Response(serializer.data)
    def post(self,request):
         serializer= AllTaskSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.validated_data
         return Response(serializer.data,status=status.HTTP_201_CREATED)  
    
# @api_view(['GET','POST'])
# def Task_list(request):
#     if request.method =='GET':
      
#     elif request.method =='POST':
       
        
class Task_Detail(APIView):
     def get(self,request,id):
        task=get_object_or_404(Task,pk=id)
        serializer=TaskSerializer(task)
        return Response(serializer.data)  
     def put(self,request,id) :
        task=get_object_or_404(Task,pk=id)
        serializer=TaskSerializer(task,data=request.data) 
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data)

# @api_view(['GET','PUT','PATCH'])
# def Task_Detail(request,id):
    
        
    