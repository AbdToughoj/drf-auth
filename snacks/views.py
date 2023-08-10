from django.shortcuts import render
from .models import Snack
from django.shortcuts import render
from .serializers import SnackSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .permissions import PurchaserOnly

class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes =[PurchaserOnly]