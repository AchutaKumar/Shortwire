from rest_framework import serializers

class ShortenRequestSerializer(serializers.Serializer):
    longUrl = serializers.CharField(max_length=2048)