from .models import User

class EmailAuthBackend:
    """
    Authenticate using an Email .
    """

    def authenticate(self,request,phone_number=None,password=None):
        try:
            user = User.objects.get(email=phone_number)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
