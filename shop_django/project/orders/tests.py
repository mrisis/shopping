from django.test import TestCase
from .models import Order , OrderItem , Coupon
from accounts.models import User
from home.models import Product

class TestOrderModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='rezaamin8889@gmail.com',
            phone_number='09123456789',
            full_name='reza amin',
            password='123456789'

        )
        self.order = Order.objects.create(
            user=self.user,
            paid=True,
            discount=10
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.paid, True)
        self.assertEqual(self.order.discount, 10)
        self.assertEqual(self.order.get_total_price(), 0)
        self.assertEqual(str(self.order), f'{self.user} - {self.order.id}')

    def test_order_str(self):
        self.assertEqual(str(self.order), f'{self.user} - {self.order.id}')

    def test_order_get_total_price(self):
        self.assertEqual(self.order.get_total_price(), 0)


# class TestOrderItemModel(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             email='rezaamin8889@gmail.com',
#             phone_number='09123456789',
#             full_name='reza amin',
#             password='123456789'
#
#         )
#         self.order = Order.objects.create(
#             user=self.user,
#             paid=True,
#             discount=10
#         )
#         self.product = Product.objects.create(



class TestCouponModel(TestCase):
    def setUp(self):
        self.coupon = Coupon.objects.create(
            code='test',
            valid_form='2020-12-12',
            valid_to='2020-12-12',
            discount=10,
            active=True
        )

    def test_coupon_creation(self):
        self.assertEqual(self.coupon.code, 'test')
        self.assertEqual(self.coupon.valid_form, '2020-12-12')
        self.assertEqual(self.coupon.valid_to, '2020-12-12')
        self.assertEqual(self.coupon.discount, 10)
        self.assertEqual(self.coupon.active, True)
        self.assertEqual(str(self.coupon), self.coupon.code)

    def test_coupon_str(self):
        self.assertEqual(str(self.coupon), self.coupon.code)





