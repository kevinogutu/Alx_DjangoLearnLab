from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    # ---
    # Step 2: Set Up Testing Environment
    # ---
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        This runs once for the entire test class.
        """
        # Create a user for authentication
        cls.user = User.objects.create_user(
            username='testuser', 
            password='testpassword123'
        )
        
        # Create a token for the user
        cls.token = Token.objects.create(user=cls.user)

        # Create initial books for testing GET, filter, search, etc.
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
        
        # Define the URL names (matching your api/urls.py)
        cls.list_url = reverse('book-list')
        cls.create_url = reverse('book-create')
        cls.detail_url = reverse('book-detail', args=[cls.book1.pk])
        cls.update_url = reverse('book-update', args=[cls.book1.pk])
        cls.delete_url = reverse('book-delete', args=[cls.book1.pk])

    def setUp(self):
        """
        Set up client authentication for each test.
        This runs before every single test method.
        """
        # Authenticate the client for all tests by default
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # ---
    # Step 3: Test Cases - Read-Only (Public Access)
    # ---
    def test_list_books_unauthenticated(self):
        """
        Ensure unauthenticated users CAN list books. (IsAuthenticatedOrReadOnly)
        """
        self.client.logout() # Log out the default authenticated user
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_detail_book_unauthenticated(self):
        """
        Ensure unauthenticated users CAN retrieve a single book. (IsAuthenticatedOrReadOnly)
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
        """
        self.client.logout()
        data = {'title': 'Unauthorized Book', 'author': 'Anon', 'isbn': '1111111111111'}
        response = self.client.post(self.create_url, data, format='json')
        
        # Expect 401 Unauthorized (since we use TokenAuth)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_unauthenticated(self):
        """
        Ensure unauthenticated users CANNOT update a book.
        """
        self.client.logout()
        data = {'title': 'Updated Title', 'author': 'Anon', 'isbn': '1111111111111'}
        response = self.client.put(self.update_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_unauthenticated(self):
        """
        Ensure unauthenticated users CANNOT delete a book.
        """
        self.client.logout()
        response = self.client.delete(self.delete_url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)

    # ---
    # Step 3: Test Cases - CRUD (Authenticated)
    # ---
    def test_create_book_authenticated(self):
        """
        Ensure authenticated users CAN create a book.
        """
        data = {
            'title': 'A New Hope',
            'author': 'George Lucas',
            'isbn': '1234567890123',
            'published_date': '1977-05-25'
        }
        response = self.client.post(self.create_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'A New Hope')

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users CAN update a book (using PUT).
        """
        data = {
            'title': 'Dune (Updated)',
            'author': 'Frank Herbert',
            'isbn': '9780441172719', # PUT requires all fields
            'published_date': '1965-08-01'
        }
        response = self.client.put(self.update_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Refresh the object from the database to check changes
        self.book1.refresh_from_db() 
        self.assertEqual(self.book1.title, 'Dune (Updated)')

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users CAN delete a book.
        """
        response = self.client.delete(self.delete_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    # ---
    # Step 1 & 3: Test Cases - Filtering, Searching, and Ordering
    # ---
    def test_filter_by_publication_year(self):
        """
        Test filtering by 'publication_year' on the list endpoint.
        """
        # 
        url = f"{self.list_url}?publication_year=1965"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')

    def test_filter_by_author_icontains(self):
        """
        Test filtering by partial 'author' match.
        """
        url = f"{self.list_url}?author=asimov" # Case-insensitive
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Foundation')

    def test_search_by_title(self):
        """
        Test searching by 'search' parameter on the title.
        """
        url = f"{self.list_url}?search=dune"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')
        
    def test_search_by_author(self):
        """
        Test searching by 'search' parameter on the author.
        """
        url = f"{self.list_url}?search=herbert"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')

    def test_ordering_by_title_ascending(self):
        """
        Test ordering by 'title' ascending (A-Z).
        """
        url = f"{self.list_url}?ordering=title"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Dune') # D
        self.assertEqual(response.data[1]['title'], 'Foundation') # F

    def test_ordering_by_published_date_descending(self):
        """
        Test ordering by 'published_date' descending (newest first).
        """
        url = f"{self.list_url}?ordering=-published_date"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Dune') # 1965
        self.assertEqual(response.data[1]['title'], 'Foundation') # 1951