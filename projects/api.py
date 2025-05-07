from rest_framework import viewsets, permissions
from .models import EnglishWord
from .serializers import EnglishWordSerializer

class EnglishWordViewSet(viewsets.ModelViewSet):
    queryset = EnglishWord.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EnglishWordSerializer