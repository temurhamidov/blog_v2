from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class LoginRequrmentMixins(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('user:login_view')
        return super(LoginRequrmentMixins, self).dispatch(request, *args, **kwargs)





