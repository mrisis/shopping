from django.test import TestCase
from .models import User,OtpCode

class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email= 'rezaamin8889@gmail.com',
            phone_number= '09123456789',
            full_name= 'reza amin',
            password= '123456789'

        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'rezaamin8889@gmail.com')
        self.assertEqual(self.user.phone_number, '09123456789')
        self.assertEqual(self.user.full_name, 'reza amin')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_user_str(self):
        self.assertEqual(str(self.user) , 'rezaamin8889@gmail.com')

    def test_uesr_is_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_has_perm(self):
        self.assertTrue(self.user.has_perm('accounts.view_user'))

    def test_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms('accounts'))



class TestOtpCode(TestCase):
    def setUp(self):
        self.otp = OtpCode.objects.create(
            phone_number= '09123456789',
            code= '123456'
        )

    def test_otp_creation(self):
        self.assertEqual(self.otp.phone_number, '09123456789')
        self.assertEqual(self.otp.code, '123456')

    def test_otp_str(self):
        self.assertEqual(str(self.otp) , '09123456789 - 123456 - 2020-02-15 17:36:18.633000+00:00')
