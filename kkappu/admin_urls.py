from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.resolvers import URLPattern, URLResolver

from wagtail.admin.urls import urlpatterns as orig_urlpatterns

from yholics.views import login_gateway


def login_router(request):
    if request.user.is_authenticated:
        if request.user.has_perm("wagtailadmin.access_admin"):
            return HttpResponseRedirect(reverse("wagtailadmin_home"))
        else:
            # This means the user is authenticated but doesn't have permission
            # to access Wagtail admin. Just redirect to the default page.
            # TODO: display a message?
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return login_gateway(request)


def _process_urlpatterns(patterns):
    result = []
    # Remove password reset view and replace login view
    for pattern in patterns:
        if isinstance(pattern, URLResolver):
            result.append(URLResolver(
                pattern.pattern,
                _process_urlpatterns(pattern.url_patterns),
                pattern.default_kwargs,
                pattern.app_name,
                pattern.namespace,
            ))
        elif isinstance(pattern, URLPattern):
            if pattern.name == "wagtailadmin_login":
                result.append(URLPattern(
                    pattern.pattern,
                    login_router,
                    pattern.default_args,
                    pattern.name,
                ))
            elif pattern.name is None or not pattern.name.startswith("wagtailadmin_password_reset"):
                result.append(pattern)
    return result


urlpatterns = _process_urlpatterns(orig_urlpatterns)
