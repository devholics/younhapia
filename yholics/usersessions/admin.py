from django.contrib import admin
from django.utils.timezone import now

from .models import UserSession


class ExpiredFilter(admin.SimpleListFilter):
    title = 'Is Valid'
    parameter_name = 'active'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Active'),
            ('0', 'Expired'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(expire_date__gt=now())
        elif self.value() == '0':
            return queryset.filter(expire_date__lte=now())


class OwnerFilter(admin.SimpleListFilter):
    title = 'Owner'
    parameter_name = 'owner'

    def lookups(self, request, model_admin):
        return (
            ('my', 'Self'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'my':
            return queryset.filter(user=request.user)


class UserSessionAdmin(admin.ModelAdmin):
    list_display = "ip", "user", "is_valid"
    list_filter = ExpiredFilter, OwnerFilter
    exclude = 'session_key',
    list_select_related = ['user']

    def is_valid(self, obj):
        return obj.expire_date > now()
    is_valid.boolean = True


admin.site.register(UserSession, UserSessionAdmin)
