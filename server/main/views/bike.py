from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import ListAPIView
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models.bike import Bike, BikeAccess, BikeAccessRequest, BikeStatus, RideSummary
from ..serializers.bike import (BikeSerializer, BikeAccessSerializer, BikeAccessRequestSerializer,
                                        BikeStatusSerializer, RideSummarySerializer, DriverAccessSerializer)

class BikeView(ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = (AllowAny,)
    

class BikeAccessView(ModelViewSet):
    serializer_class = BikeAccessSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return BikeAccess.objects.filter(bike=self.kwargs['bike_pk'])

class BikeAccessRequestView(ModelViewSet):
    serializer_class = BikeAccessRequestSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return BikeAccessRequest.objects.filter(bike=self.kwargs['bike_pk'])

class BikeStatusView(ModelViewSet):
    serializer_class = BikeStatusSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return BikeStatus.objects.filter(bike=self.kwargs['bike_pk'])

class RideSummaryView(ModelViewSet):
    serializer_class = RideSummarySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return RideSummary.objects.filter(bike=self.kwargs['bike_pk'])

class DriverBikes(ListAPIView):
    serializer_class = DriverAccessSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        bikes = BikeAccess.objects.filter(Q(user=self.request.user)| Q(bike__admin=self.request.user) )
        return bikes

