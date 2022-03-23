from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "full_name", "is_staff", "is_active"]
    exclude = ["password"]
    list_display_links = ["id", "email"]
    list_filter = ["is_staff", "is_active"]
    search_fields = ["email"]
    show_full_result_count = True


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img']

    class Meta:
        pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Meta:
        pass
