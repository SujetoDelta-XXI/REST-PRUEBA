from rest_framework import serializers
from .models import EnglishWord

class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWord
        fields = "__all__"
        read_only_fields = ['id', 'date_added']