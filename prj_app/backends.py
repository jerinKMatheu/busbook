from django.contrib.auth.backends import BaseBackend
from .models import register  # Import your custom user model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = register.objects.get(email=email)
            print(f'user: {user}')
            if user.password == password:
                return user
            else:
                return None
        except register.DoesNotExist:
            return None