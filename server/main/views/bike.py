from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny
from ..models.bike import Bike, BikeAccess, BikeAccessRequest, BikeStatus, RideSummary
from ..serializers.bike import BikeSerializer, BikeAccessSerializer, BikeAccessRequestSerializer, BikeStatusSerializer, RideSummarySerializer

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
    queryset = BikeStatus.objects.all()
    serializer_class = BikeStatusSerializer
    permission_classes = (AllowAny,)

class RideSummaryView(ModelViewSet):
    queryset = RideSummary.objects.all()
    serializer_class = RideSummarySerializer
    permission_classes = (AllowAny,)