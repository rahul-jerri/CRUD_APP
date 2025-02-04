from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Author
from ..serializers import AuthorSerializer

class AuthorListCreateViewTests(TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.client = APIClient()
        self.author_url = '/authors/'  # Replace with the actual endpoint for the view

        # Sample author data
        self.valid_data = {
            "name": "Jane Austen",
            "birth_date": "1775-12-16",
        }
        self.invalid_data = {
            "name": "",
            "birth_date": "invalid-date",
        }

        # Create some authors for testing GET
        self.author1 = Author.objects.create(name="Mark Twain", birth_date="1835-11-30")
        self.author2 = Author.objects.create(name="Charles Dickens", birth_date="1812-02-07")

    def test_get_authors(self):
        """Test retrieving a list of authors."""
        response = self.client.get(self.author_url)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_author_success(self):
        """Test creating an author with valid data."""
        response = self.client.post(self.author_url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the author was created
        self.assertEqual(Author.objects.count(), 3)
        self.assertEqual(Author.objects.last().name, "Jane Austen")

    def test_create_author_failure(self):
        """Test creating an author with invalid data."""
        response = self.client.post(self.author_url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify that no new author was created
        self.assertEqual(Author.objects.count(), 2)
