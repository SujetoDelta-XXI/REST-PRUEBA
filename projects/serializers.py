from rest_framework import serializers
from .models import EnglishWord

class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model: EnglishWord
        fields = "__all_"
        read_only_fields = ['id', 'date_added']