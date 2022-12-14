import random
from celery import shared_task
from .models import youtube
import requests
api="https://youtube.googleapis.com/youtube/v3/search?part=snippet&type=video&order=date&maxResults=10&q=football&key=AIzaSyCQ821zBB8iCIgxqAZO3l0fuXjXTWXZQ30"
# 
@shared_task
def add():
    res=requests.get(api)
    for i in res.json()["items"]:
        db_insert=youtube(thumbnails_URL=res["snippet"]["thumbnails"]["medium"]["url"],task=i["snippet"]['title'],description=i["snippet"]["description"],channelName=i["snippet"]["channelTitle"])
        db_insert.save()
    return "data added sucessfully"

