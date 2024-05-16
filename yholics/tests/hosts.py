# A dummy hostconf for testing

from django_hosts import host

host_patterns = [host(r"www", "yholics.tests.urls", name="www")]
