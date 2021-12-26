from rest_framework import  serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task.models import TodoTask
from task.api.serializers import TodoTaskSerializer

@api_view(['GET'])
def task_list(request):
    if request.method =="GET":
        query=TodoTask.objects.all()
        serializer=TodoTaskSerializer(query,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_task_detail(request,id):
    try:
        task=TodoTask.objects.get(pk=id)
    except TodoTask.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method=="GET":
        serializer=TodoTaskSerializer(task)
        return Response(serializer.data)     

@api_view(['PUT'])
def api_task_update(request,id):
    try:
        task=TodoTask.objects.get(id=id)
    except TodoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data={}    
    if request.method=='PUT':
       serializer=TodoTaskSerializer(task,data=request.data)            
       if serializer.is_valid():
          serializer.save()
          data['anjamshod']="update anjam shod"
          return Response(data=data) 
         
