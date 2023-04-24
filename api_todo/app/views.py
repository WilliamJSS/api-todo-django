from .models import Todo
from .serializers import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)
