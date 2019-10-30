from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


def index(request):
    return HttpResponseRedirect('/admin')


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Endoscpoists to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
