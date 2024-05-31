# A dummy hostconf for testing

from django.conf import settings

from django_hosts import host

host_patterns = [host(r"www", settings.ROOT_URLCONF, name="www")]
