from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomUser, Session, Turn, Donation, Category, VolunteerRequest
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Session)
admin.site.register(Turn)
admin.site.register(Donation)
admin.site.register(Category)
admin.site.register(VolunteerRequest)
