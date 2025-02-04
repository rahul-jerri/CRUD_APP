# myapp/tests/test_borrower.py
from rest_framework.test import APITestCase
from ..models import Borrower
from rest_framework import status

class BorrowerTests(APITestCase):
    def setUp(self):
        self.borrower_data = {
            "name": "Test Borrower",
            "email": "borrower@example.com",
            "phone_number": "1234567890",
            "membership_date": "2025-01-01"
        }

    def test_create_borrower(self):
        response = self.client.post('/borrowers/', self.borrower_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Borrower.objects.count(), 1)

    def test_get_borrower(self):
        borrower = Borrower.objects.create(**self.borrower_data)
        response = self.client.get(f'/borrowers/{borrower.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], borrower.name)

    def test_update_borrower(self):
        borrower = Borrower.objects.create(**self.borrower_data)
        updated_data = {"name": "Updated Borrower"}
        response = self.client.put(f'/borrowers/{borrower.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        borrower.refresh_from_db()
        self.assertEqual(borrower.name, "Updated Borrower")

    def test_delete_borrower(self):
        borrower = Borrower.objects.create(**self.borrower_data)
        response = self.client.delete(f'/borrowers/{borrower.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Borrower.objects.count(), 0)
