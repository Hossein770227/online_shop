from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Product

User = get_user_model()

class ProductTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(phone_number='0921123456',full_name= 'hossein', password='12345')
        self.product1 = Product.objects.create(
            name = 'product1',
            description ='some description',
            price = 100,
            price_with_discount = 150,

        )
        
    def test_product_list_by_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_by_name(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_list_use_template(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertTemplateUsed(response, 'my_products/product_list.html')

    # def test_product_list_contain_name(self):
    #     response = self.client.get(reverse('products:product_list'))
    #     self.assertContains(response, self.product1.name)

