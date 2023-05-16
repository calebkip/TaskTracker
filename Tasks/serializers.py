from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
     
   class  Meta:
    model=Task
    fields=['title','description','assigned_to','status','progress','department']

  
   def create(self,validated_data):
     task=Task(**validated_data)
     task.other=1
     task.save()
     return task

   def update(self, instance, validated_data):
     instance.status=validated_data.get('status')
     instance.save()
     return instance
     
  
class AllTaskSerializer(serializers.ModelSerializer):
  class Meta:
    model=Task
    fields=['title','description','assigned_to','status','progress']