from rest_framework import serializers

from .models import intractive_map


class Intractive_mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = intractive_map
        # fields = ['id','title', 'author','email']
        fields = '__all__'