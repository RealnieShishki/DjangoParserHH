from django.test import TestCase
from .models import Request, Area, Vacancy, Skills
from userapp.models import Applicant
from mixer.backend.django import mixer
# Create your tests here.


class RequestTestMixer(TestCase):

    def setUp(self):
        self.request = mixer.blend(Request)
        self.post_str = mixer.blend(Request, name='test_req_str', area__name='test_category')

        def test_has_image(self):
            self.assertFalse(self.post.has_image())

        def test_some_method(self):
            self.assertFalse(self.post.some_method() == 'some method')

        def test_str(self):
            self.assertEqual(str(self.post_str), 'test_req_str, area: test_category')
