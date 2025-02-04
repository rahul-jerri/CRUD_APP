# myapp/tests/test_borrow_record.py
from rest_framework.test import APITestCase
from ..models import BorrowRecord, Book, Borrower
from datetime import date
from rest_framework import status

class BorrowRecordTests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            isbn="1234567890123",
            publication_date="2025-01-01",
            available_copies=5,
            total_copies=10,
            author_id=2
        )
        self.borrower = Borrower.objects.create(
            name="Test Borrower",
            email="borrower@example.com",
            phone_number="1234567890",
            membership_date="2025-01-01"
        )
        self.borrow_record_data = {
            "book": self.book.id,
            "borrower": self.borrower.id,
            "borrow_date": "2025-01-10",
            "return_date": "2025-01-20",
            "status": "borrowed"
        }

    def test_create_borrow_record(self):
        response = self.client.post('/borrow_records/', self.borrow_record_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BorrowRecord.objects.count(), 1)

    def test_get_borrow_record(self):
        borrow_record = BorrowRecord.objects.create(**self.borrow_record_data)
        response = self.client.get(f'/borrow_records/{borrow_record.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], borrow_record.status)

    def test_update_borrow_record(self):
        borrow_record = BorrowRecord.objects.create(**self.borrow_record_data)
        updated_data = {"status": "returned"}
        response = self.client.put(f'/borrow_records/{borrow_record.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        borrow_record.refresh_from_db()
        self.assertEqual(borrow_record.status, "returned")

    def test_delete_borrow_record(self):
        borrow_record = BorrowRecord.objects.create(**self.borrow_record_data)
        response = self.client.delete(f'/borrow_records/{borrow_record.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BorrowRecord.objects.count(), 0)

    def test_borrow_book_with_no_copies(self):
        self.book.available_copies = 0
        self.book.save()
        response = self.client.post('/borrow_records/', self.borrow_record_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(BorrowRecord.objects.count(), 0)
