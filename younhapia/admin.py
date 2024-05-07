from functools import update_wrapper

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


class YounhapiaAdminSite(admin.AdminSite):
    site_header = "Younhapia administration"
    site_title = "Younhapia admin"
    index_title = "Administration"

    def admin_view(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            if not request.user.is_authenticated:
                if request.path == reverse("admin:logout", current_app=self.name):
                    index_path = reverse("admin:index", current_app=self.name)
                    return HttpResponseRedirect(index_path)
                from django.contrib.auth.views import redirect_to_login

                return redirect_to_login(request.get_full_path())
            if not self.has_permission(request):
                # TODO: attach a message
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            return view(request, *args, **kwargs)

        if not cacheable:
            inner = never_cache(inner)
        # See django.contrib.admin.sites.
        if not getattr(view, "csrf_exempt", False):
            inner = csrf_protect(inner)
        return update_wrapper(inner, view)
