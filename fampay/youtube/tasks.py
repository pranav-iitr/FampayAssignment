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
        print(i)
        db_insert=youtube(thumbnails_URL=i["snippet"]["thumbnails"]["medium"]["url"],title=i["snippet"]['title'],description=i["snippet"]["description"],channelName=i["snippet"]["channelTitle"])
        db_insert.save()
    return "data added sucessfully"

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as the `sum_list_numbers` task
    return sum(numbers)
