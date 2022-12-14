from django.shortcuts import render
from .serializer import YoutubeSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .models import youtube
from rest_framework.pagination import PageNumberPagination

from rest_framework import filters

class YoutubeListApiView(ListAPIView):
    serializer_class=YoutubeSerializer
    queryset=youtube.objects.all()
    pagination_class=PageNumberPagination


class YoutubeSearchAPIView(ListAPIView):
    search_fields = ['title','description']
    filter_backends = (filters.SearchFilter,)
    queryset = youtube.objects.all()
    serializer_class = YoutubeSerializer
# Create your views here.
