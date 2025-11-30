from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# We no longer need the Token model for this test style
# from rest_framework.authtoken.models import Token 
from .models import Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints, using session-based authentication.
    """

    # ---
    # Step 2: Set Up Testing Environment
    # ---
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        # Create a user for authentication
        cls.username = 'testuser'
        cls.password = 'testpassword123'
        cls.user = User.objects.create_user(
            username=cls.username, 
            password=cls.password
        )
        
        # We don't need to create a token if we're using client.login()

        # Create initial books for testing
        cls.book1 = Book.objects.create(
            title="Dune",
            author="Frank Herbert",
            isbn="9780441172719",
            published_date="1965-08-01"
        )
        cls.book2 = Book.objects.create(
            title="Foundation",
            author="Isaac Asimov",
            isbn="9780553293357",
            published_date="1951-06-01"
        )
        
        # Define the URL names
        cls.list_url = reverse('book-list')
        cls.create_url = reverse('book-create')
        cls.detail_url = reverse('book-detail', args=[cls.book1.pk])
        cls.update_url = reverse('book-update', args=[cls.book1.pk])
        cls.delete_url = reverse('book-delete', args=[cls.book1.pk])

    def setUp(self):
        """
        Set up client authentication for each test using session login.
        """
        # Authenticate the client using session-based login
        self.client.login(username=self.username, password=self.password)

    # ---
    # Step 3: Test Cases - Read-Only (Public Access)
    # ---
    def test_list_books_unauthenticated(self):
        """
        Ensure unauthenticated users CAN list books.
        """
        self.client.logout() # Log out the default authenticated user
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_detail_book_unauthenticated(self):
        """
        Ensure unauthenticated users CAN retrieve a single book.
        """
        self.client.logout()
        response = self.client.get(self.detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ---
    # Step 3: Test Cases - Write Endpoints (Permissions)
    # ---
    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users CANNOT create a book.