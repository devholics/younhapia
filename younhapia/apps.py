from django.contrib.admin.apps import AdminConfig


class YounhapiaAdminConfig(AdminConfig):
    default_site = "younhapia.admin.YounhapiaAdminSite"
