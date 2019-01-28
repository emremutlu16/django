from api.models import UserLogin
from django.middleware.security import MiddlewareMixin
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class ApiTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if not request.user.is_authenticated and 'admin' not in request.META['PATH_INFO']:
            raise AuthenticationFailed('LOGIN PLEASE')
        elif not request.user.is_authenticated and 'admin' in request.META['PATH_INFO']:
            pass
        elif request.user.is_authenticated and 'admin' not in request.META['PATH_INFO']:
            user = User.objects.get(username=request.user)
            if not UserLogin.objects.filter(user=user).exists():
                raise AuthenticationFailed('GET TOKEN PLEASE')
