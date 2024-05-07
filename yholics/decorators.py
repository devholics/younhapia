from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required


def staff_member_required_or_fail(
    view_func=None,
    redirect_field_name=REDIRECT_FIELD_NAME,
    login_url=settings.LOGIN_URL,
    fail_url=settings.LOGIN_REDIRECT_URL,
):
    return login_required(
        staff_member_required(view_func, redirect_field_name=None, login_url=fail_url),
        redirect_field_name=redirect_field_name,
        login_url=login_url,
    )
