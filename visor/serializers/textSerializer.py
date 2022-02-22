from rest_framework import serializers

class TextSerializer(serializers.Serializer):
    content = serializers.ListField(child=serializers.CharField())
    fromPage = serializers.IntegerField(max_value=1000, min_value=0)
    toPage = serializers.IntegerField(max_value=2000, min_value=0)