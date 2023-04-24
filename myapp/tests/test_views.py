from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import Category, Blog
from user.models import User


class HomeViewTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(
            name='test'
        )
        self.user = User.objects.create_user(
            username='test',
            password='12345678',
            email='test@mail.com'
        )
        self.blog = Blog.objects.create(
            title='Test title',
            category=self.category,
            author=self.user,
            text='text text'
        )
        self.url = reverse('myapp:home')
        self.client = Client()
        self.response = self.client.get(self.url)


    def test_view_status_code_200(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_context_data(self):
        self.assertTrue('blogs' in self.response.context)
        self.assertFalse('objects' in self.response.context)