from django.shortcuts import redirect


LEGACY_BASE_URL = "http://old.ernir.net"


def blog_redirect(request):
    return redirect(f"{LEGACY_BASE_URL}/blog")


def vtp_redirect(request):
    return redirect(f"{LEGACY_BASE_URL}/vanciantopsionics")
