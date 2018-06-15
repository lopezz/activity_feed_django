from django.contrib import admin
from django.contrib.auth.models import User
from .models import FeedItem, RegisteredUser
# Register your models here.

class UserAdmin(admin.StackedInline):
    model = User
    extra = 0

class RegisteredUserAdmin(admin.ModelAdmin):
    inlines = [User]

admin.site.register(RegisteredUser)
admin.site.register(FeedItem)