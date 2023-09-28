from django.test import TestCase
from home.models import Product , Category

class Test_Category_Model(TestCase):
    def setUp(self):
        self.category = Category.objects.create(sub_category=None , is_sub=False , name='test' , slug='test')

    def test_category_model(self):
        self.assertEqual(self.category.name , 'test')
        self.assertEqual(self.category.slug , 'test')
        self.assertEqual(self.category.is_sub , False)
        self.assertEqual(self.category.sub_category , None)

    def test_category_model_str(self):
        self.assertEqual(str(self.category) , 'test')

    def test_category_model_get_absolute_url(self):
        self.assertEqual(self.category.get_absloute_url() , '/category/test/')



class Test_product_model(TestCase):
    def setUp(self):
        self.category = Category.objects.create(sub_category=None , is_sub=False , name='test' , slug='test')
        self.product = Product.objects.create(name='test' , slug='test' , description='test' , price=100 , availabel=True)

    def test_product_model(self):
        self.assertEqual(self.product.name , 'test')
        self.assertEqual(self.product.slug , 'test')
        self.assertEqual(self.product.description , 'test')
        self.assertEqual(self.product.price , 100)
        self.assertEqual(self.product.availabel , True)

    def test_product_model_str(self):
        self.assertEqual(str(self.product) , 'test')

    def test_product_model_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url() , '/product/test/')

    def test_product_model_category(self):
        self.product.category.add(self.category)
        self.assertEqual(self.product.category.all()[0] , self.category)
























