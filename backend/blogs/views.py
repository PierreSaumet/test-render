from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blogs.serializers import BlogsSerializer
from blogs.models import Blogs


# Create your views here.
class BlogsViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer