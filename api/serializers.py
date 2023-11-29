from rest_framework import serializers

from .models import Location, Item

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'locationName')  

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'itemName', 'date_added', 'itemLocation')  

    # itemLocation = LocationSerializer()  