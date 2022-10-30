from django.test import TestCase, RequestFactory
from django.urls import reverse

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import AnonymousUser, User

from accounts.views import profile_page, register_page, login_page
from listing.views import saved_page
# Create your tests here.

class AuthTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12tEst12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_successful_login(self):
        user = authenticate(username='test', password='12tEst12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class RestrictUnauthTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_restrict_unauth_profile_page(self):
        request = self.factory.get(reverse('profile'))
        request.user = self.user
        response = profile_page(request)
        self.assertEqual(response.status_code, 302)

    def test_restrict_unauth_saved_page(self):
        request = self.factory.get(reverse('saved'))
        request.user = self.user
        response = saved_page(request)
        self.assertEqual(response.status_code, 302)

class RestrictAuthTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User()

    def test_restrict_auth_register_page(self):
        request = self.factory.get(reverse('register'))
        request.user = self.user
        response = register_page(request)
        self.assertEqual(response.status_code, 302)

    def test_restrict_auth_login_page(self):
        request = self.factory.get(reverse('login'))
        request.user = self.user
        response = login_page(request)
        self.assertEqual(response.status_code, 302)
