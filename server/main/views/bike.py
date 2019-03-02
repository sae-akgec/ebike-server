from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models.bike import Bike, BikeAccess, BikeAccessRequest, BikeStatus, RideSummary
from ..serializers.bike import (BikeSerializer, BikeAccessSerializer, BikeAccessRequestSerializer,
                                        BikeStatusSerializer, RideSummarySerializer, DriverAccessSerializer,
                                        RideHistorySerializer, DriverHistorySerializer, BikeAccessesSerializer)

class BikeView(ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = (AllowAny,)
    

class BikeAccessView(ModelViewSet):
    serializer_class = BikeAccessSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return BikeAccessesSerializer
        return super(BikeAccessView, self).get_serializer_class()

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

    
    def get_serializer_class(self):
        if self.action == 'list':
            return RideHistorySerializer
        return super(RideSummaryView, self).get_serializer_class()

    def get_queryset(self):
        return RideSummary.objects.filter(bike=self.kwargs['bike_pk'])

class DriverBikes(ListAPIView):
    serializer_class = DriverAccessSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        bikes = BikeAccess.objects.filter(user=self.request.user )
        return bikes

class DriverHistory(ListAPIView):
    serializer_class = DriverHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        bikes = RideSummary.objects.filter(driver=self.request.user)
        return bikes

