from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Volunteer, Organization, Session, Turn, Donation, Category
# Register your models here.
admin.site.register(Volunteer, UserAdmin)
admin.site.register(Organization)
admin.site.register(Session)
admin.site.register(Turn)
admin.site.register(Donation)
admin.site.register(Category)