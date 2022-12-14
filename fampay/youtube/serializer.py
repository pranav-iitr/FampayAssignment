from rest_framework import serializers

class YoutubeSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=400)
    description = serializers.CharField(max_length=400)
    thumbnails_URL = serializers.URLField()
    channelName = serializers.CharField(max_length=50)
