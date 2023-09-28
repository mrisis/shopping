from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

def send_sms_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('5347617833396B334D6734396879423341463754386B4A643562504E6E2B574D614A6F4D6C7644515141513D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'your code {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
	    return self.request.user.is_authenticated and self.request.user.is_admin