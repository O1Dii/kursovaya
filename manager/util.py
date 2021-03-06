from django.contrib import auth
from django.shortcuts import render


class AuthCheckMixin:
    def check_perm_manager(self, request):
        if not auth.get_user(request).is_anonymous:
            if auth.get_user(request).rating is None:
                return None
        return render(request, 'access_deny.html', {})

    def check_perm_expert(self, request):
        if not auth.get_user(request).is_anonymous:
            if auth.get_user(request).rating is not None:
                return None
        return render(request, 'access_deny.html', {})
