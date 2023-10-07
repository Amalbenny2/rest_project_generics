from django.shortcuts import render
from turfapp.models import venue,customers
from turfapp.serializer import Venueserializer,Customersserializer
from rest_framework import generics

# Create your views here.


class venue_add(generics.ListCreateAPIView):
    queryset = venue.objects.all()
    serializer_class = Venueserializer

class venue_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = venue.objects.all()
    serializer_class = Venueserializer


class customer(generics.ListCreateAPIView):
    queryset = customers.objects.all()
    serializer_class = Customersserializer

class customer_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = customers.objects.all()
    serializer_class = Customersserializer

