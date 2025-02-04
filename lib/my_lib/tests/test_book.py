# myapp/tests/test_book.py
from rest_framework.test import APITestCase
from ..models import Book, Author
from rest_framework import status

class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "isbn": "1234567890123",
            "publication_date": "2025-01-01",
            "available_copies": 5,
            "total_copies": 10,
            "author": self.author.author_id
        }

    def test_create_book(self):
        response = self.client.post('/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

    def test_get_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.get(f'/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {"title": "Updated Book"}
        response = self.client.put(f'/books/{book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Updated Book")

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(f'/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
