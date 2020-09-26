from django.shortcuts import get_object_or_404
from rest_framework import generics, status, serializers
from rest_framework.response import Response

from .models import *
from .serializers import NodeSerializer, NodeUsersSerializer


class NodeAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API for get, update and delete a node"""
    name = "nodes"
    queryset = PioNode.objects.all()
    serializer_class = NodeSerializer

    def get_object(self):
        pk = self.kwargs.get("pk", None)
        return get_object_or_404(PioNode, id=pk)


class UsersByNodeListAPIView(generics.ListAPIView):
    """Get all users that belong to node"""
    name = "users-by-node"
    queryset = PioNode.objects.all()
    serializer_class = NodeUsersSerializer


# class MentoringAPIView(generics.RetrieveUpdateDestroyAPIView):
#     """API for get, update and delete a mentoring"""
#     name = "mentorings"
#     queryset = ''
#     serializer_class = ''


# class MentoringByUserListView(generics.ListAPIView):
#     """Get a list of all mentorings for a user"""
#     name = "mentorings-user"
#     queryset = ''
#     serializer_class = ''

# class MentoringByNodeListView(generics.ListAPIView):
#     """Get all mentorings that belong to node"""
#     name = "mentorings-by-node"
#     queryset = ''
#     serializer_class = ''


# class MentoringCreateView(generics.CreateAPIView):
#     """Create mentoring between a mentor and learner"""
#     name = "mentoring-create"
#     queryset = ''
#     serializer_class = ''
