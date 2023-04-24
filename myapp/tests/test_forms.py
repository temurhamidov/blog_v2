from django.test import TestCase
from myapp.forms import CommentForm, BlogForm

class CommentFormTest(TestCase):
    def test_forms(self):
        data1 = {'text': "First_comment", 'rating': 5}
        form = CommentForm(data=data1)
        self.assertTrue(form.is_valid())

        data1 = {'text': "First_comment", 'rating1': 5}
        form = CommentForm(data=data1)
        self.assertFalse(form.is_valid())


