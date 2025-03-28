from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Organization
from django.utils.translation import gettext_lazy as _

# Register your models here.
class BaseUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", 'username',"password" )}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    'is_organizor',
                    'is_agent',
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

admin.site.register(User, BaseUserAdmin)
admin.site.register(Organization)