from django.conf.urls import re_path, include, url
from rest_framework_nested import routers
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from .views.accounts import (UserEmailVerificationAPIView, UserProfileAPIView, UserRegistrationAPIView,
                           UserLoginView, PasswordResetAPIView, PasswordResetConfirmView, UpdateProfileAPIView)
from .views.bike import BikeAccessRequestView, BikeView, BikeAccessView, RideSummaryView, BikeStatusView, DriverBikes, DriverHistory

bike_router = routers.DefaultRouter()
bike_router.register(r'bikes', BikeView)

bike_nested_router = routers.NestedDefaultRouter(bike_router, r'bikes', lookup='bike')

bike_nested_router.register(r'access', BikeAccessView, base_name='bike-access')
bike_nested_router.register(r'request', BikeAccessRequestView, base_name='bike-access-request')
bike_nested_router.register(r'summary', RideSummaryView, base_name='bike-summary')
bike_nested_router.register(r'status', BikeStatusView, base_name='bike-status')
# bike_router.register(r'{pk}/request', BikeAccessRequestView)
# bike_router.register(r'{pk}/summary', RideSummaryView)
# bike_router.register(r'{pk}/status', BikeStatusView)


urlpatterns = [
   url(r'^docs/', include_docs_urls(title="api-doc", public=True, permission_classes=[])),
   url(r'^auth/login/', UserLoginView.as_view(), name='login'),
   url(r'^auth/register/', UserRegistrationAPIView.as_view(), name='regsiter'),
   url(r'^auth/verify/(?P<verification_key>.+)/$', UserEmailVerificationAPIView.as_view(), name='email_verify'),
   url(r'^auth/password_reset/$', PasswordResetAPIView.as_view(), name='password_change'),
   url(r'^auth/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   url(r'^user/bikes', DriverBikes.as_view(), name='driver_bikes'),
   url(r'^user/history', DriverHistory.as_view(), name='driver_history'),
   url(r'^user/profile/$', UserProfileAPIView.as_view(), name='user_profile'),
   url(r'^user/profile/update$', UpdateProfileAPIView.as_view(), name='user_profile'),
   url(r'^', include(bike_router.urls), name='bikes'),
   url(r'^', include(bike_nested_router.urls), name='bike'),
]