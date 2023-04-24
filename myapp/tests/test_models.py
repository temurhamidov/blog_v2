from django.test import TestCase
from django.core.exceptions import ImproperlyConfigured
from myapp.models import Category, Blog, Tag, Comment
from user.models import User


class CategoryModelTest(TestCase):
    def setUp(self) -> None:
        self.category = Category(
            name='test'
        )
    def test_get_data(self):
        self.assertNotEquals(self.category.name, 'nimadir')
        self.assertEquals(self.category.name, 'test')

    def test_object_name(self):
        self.assertTrue(str(self.category), self.category.name)


class TagModelTest(TestCase):
    def setUp(self) -> None:
        self.tag = Tag(
            name='test'
        )
    def test_get_data(self):
        self.assertEquals(self.tag.name, 'test')
        self.assertNotEquals(self.tag.name, 'test1')

class BlogModelTest(TestCase):
    def setUp(self) -> None:
        self.category = Category(
            name='test'
        )
        self.user = User(
            username='test',
            password='12345678',
            email='test@mail.com'
        )
        self.blog = Blog(
            title='Test title',
            category=self.category,
            author=self.user,
            text='text text'
        )

    def test_object_name(self):
        self.assertTrue(str(self.blog), self.blog.title)


class CommentModelTest(TestCase):
    def setUp(self) -> None:
        self.category = Category(
            name='test'
        )
        self.user = User(
            username='Ali',
            password='11223233',
            email='kjh@kjh.com',
        )
        self.blog = Blog(
            title='Test title',
            category=self.category,
            author=self.user,
            text='text text'
        )
        self.comment = Comment(
            user=self.user,
            blog=self.blog,
            text='assalomu alaykum',
            rating=5
        )
    def test_object_name(self):
        self.assertEquals(str(self.comment), self.comment.user.username)



