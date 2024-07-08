# A dummy hostconf for testing

from django_hosts import host

from younhapia.hosts import host_patterns as orig_host_patterns


host_patterns = orig_host_patterns + [
    host(r"dummy", "yholics.tests.urls", name="dummy")
]
