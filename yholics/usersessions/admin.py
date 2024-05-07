from django.contrib import admin
from django.utils.timezone import now

from .models import UserSession


class UserSessionAdmin(admin.ModelAdmin):
    list_display = "ip", "user_agent", "user", "is_valid"

    def is_valid(self, obj):
        return obj.expire_date > now()

    is_valid.boolean = True


admin.site.register(UserSession, UserSessionAdmin)
