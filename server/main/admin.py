from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField


MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
})

from .models.accounts import UserProfile
from .models.bike import Bike, BikeAccess, BikeAccessRequest, BikeStatus, RideSummary

admin.site.register(Bike, MySpecialAdmin(Bike))
admin.site.register(BikeAccess, MySpecialAdmin(BikeAccess))
admin.site.register(BikeAccessRequest, MySpecialAdmin(BikeAccessRequest))
admin.site.register(BikeStatus, MySpecialAdmin(BikeStatus))
admin.site.register(RideSummary, MySpecialAdmin(RideSummary))



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'is_active', 'has_email_verified')

    def email(self, profile):
        return profile.user.email

    def name(self, profile):
        return profile.user.first_name + " " + profile.user.last_name

    def is_active(self, profile):
        return profile.user.is_active
