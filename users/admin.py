from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, CurrencyRequest, Text


class CurrencyRequestInline(admin.TabularInline):
    model = CurrencyRequest
    extra = 0


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "id", "active_follow"]
    search_fields = ["username", "id", "active_follow"]

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("active_follow",)}),
    )

    inlines = [CurrencyRequestInline]


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ("name", "content")


class CurrencyRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "exchange_rate", "date"]
    search_fields = ["user__username"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CurrencyRequest, CurrencyRequestAdmin)
