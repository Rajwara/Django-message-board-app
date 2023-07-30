from django.test import TestCase
from .models import post
# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = post.objects.create(text = "This is a ourtest!")
        
        
    def test_model_content(self):
        self.assertEqual(self.post.text, "Tis is other test")
        