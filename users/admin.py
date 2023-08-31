from django.contrib import admin
from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "date_joined",
    ]

    search_fields = [
        "username",
        "email",
    ]
