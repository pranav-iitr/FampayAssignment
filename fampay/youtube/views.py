from django.shortcuts import render
from .serializer import YoutubeSerializer
from rest_framework.generics import ListAPIView
from .models import youtube
from rest_framework.pagination import LimitOffsetPagination

class GetList(ListAPIView):
    serializer_class=YoutubeSerializer
    queryset=youtube.objects.all()
    pagination_class=LimitOffsetPagination


# Create your views here.
