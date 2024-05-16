from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import NormalUserCreationForm

class TestAuthenticationFunctions(TestCase):
    def setUp(self):
        self.User = get_user_model()

        # URL to the sign-up page
        self.sign_up_url = reverse('signup')
        self.login_url = reverse('login')
        # Valid payload for creating a new user
        self.valid_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.valid_login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
            
    def testRetreiveLoginPage(self):
        response  = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200) 
    
    def testRetrieveLoggedOutPage(self):
        response  = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def testRetrieveSignUpPage(self):
        response = self.client.post(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        
    def test_form_used(self):
        response = self.client.get(self.sign_up_url)
        self.assertIsInstance(response.context['form'], NormalUserCreationForm)

    def test_user_creation_with_valid_data(self):
        response = self.client.post(self.sign_up_url, self.valid_data)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertEqual(self.User.objects.first().username, 'testuser')
        
    def test_user_creation_with_invalid_data(self):
        # Change the data to be invalid, e.g., passwords do not match
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'wrong'
        response = self.client.post(self.sign_up_url, invalid_data)
        self.assertEqual(self.User.objects.count(), 0)
        self.assertEqual(response.status_code, 200)  # Check if the form is re-rendered with an error

    def test_user_creation_with_duplicate_username(self):
        # Create a user first
        self.User.objects.create_user(username='testuser', password='testpassword123')
        # Attempt to create another user with the same username
        response = self.client.post(self.sign_up_url, self.valid_data)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertIn('username', response.context['form'].errors)
    
    def test_user_login(self):
        self.User.objects.create_user(username='testuser', password='testpassword123')
        # test for login in
        self.client.post(self.login_url, self.valid_login_data)
        self.assertTrue('_auth_user_id' in self.client.session)