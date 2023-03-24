from rest_framework import serializers

class PalomaSerializer(serializers.Serializer):
    color = serializers.CharField(max_length=200)
    edad = serializers.IntegerField(read_only=True)
    habitad = serializers.CharField(max_length=200)