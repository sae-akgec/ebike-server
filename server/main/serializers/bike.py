from rest_framework import serializers
from ..models.bike import Bike, BikeAccess, BikeAccessRequest, BikeStatus, RideSummary
from .accounts import ProfileUserSerializer

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'

class BikeAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeAccess
        fields = '__all__'

class BikeAccessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeAccessRequest
        fields = '__all__'

class BikeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeStatus
        fields = '__all__'

class RideSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = RideSummary
        fields = '__all__'

class RideHistorySerializer(serializers.ModelSerializer):
    driver = ProfileUserSerializer()

    class Meta:
        model = RideSummary
        fields = '__all__'

class DriverHistorySerializer(serializers.ModelSerializer):
    bike = BikeSerializer()

    class Meta:
        model = RideSummary
        fields = '__all__'

class DriverAccessSerializer(serializers.ModelSerializer):
    bike = BikeSerializer()
    class Meta:
        model = BikeAccess
        fields = '__all__'
