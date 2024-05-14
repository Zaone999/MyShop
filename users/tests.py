from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

class TestAuthenticationFunctions(TestCase):
    def setUp(self):
        self.User = get_user_model()

        # URL to the sign-up page
        self.url = reverse('signup')
        # Valid payload for creating a new user
        self.valid_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'role': 'user',
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
        response = self.client.get(self.url)
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_user_creation_with_valid_data(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertEqual(self.User.objects.first().username, 'testuser')
        
    def test_user_creation_with_invalid_data(self):
        # Change the data to be invalid, e.g., passwords do not match
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'wrong'
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(self.User.objects.count(), 0)
        self.assertEqual(response.status_code, 200)  # Check if the form is re-rendered with an error

    def test_user_creation_with_duplicate_username(self):
        # Create a user first
        self.User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')
        # Attempt to create another user with the same username
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertIn('username', response.context['form'].errors)