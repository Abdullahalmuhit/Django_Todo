from rest_framework import serializers
from todoapp.models import ToDo


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['name', 'write']