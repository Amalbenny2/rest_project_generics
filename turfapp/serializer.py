from rest_framework import serializers
from turfapp.models import venue,customers

class Venueserializer(serializers.ModelSerializer):
    class Meta:
        model=venue
        fields='__all__'


class Customersserializer(serializers.ModelSerializer):
    class Meta:
        model=customers
        fields='__all__'