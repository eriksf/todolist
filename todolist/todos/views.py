from rest_framework import viewsets
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
