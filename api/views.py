from rest_framework import generics
from todoapp.models import ToDo
from .serializers import QuoteSerializer


class QuoteAPIView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = QuoteSerializer
