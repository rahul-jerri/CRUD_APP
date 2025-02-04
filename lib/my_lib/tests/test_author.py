from rest_framework.test import APITestCase
from rest_framework import status
from my_lib.models import Author
from my_lib.serializers import AuthorSerializer

class AuthorTests(APITestCase):
    def setUp(self):
        self.author_data = {
            'name': 'Test Author',
            'date_of_birth': '1970-01-01',
            'bio': 'This is a test author bio.'
        }

    def test_create_author(self):
        response = self.client.post('/authors/', self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.author_data['name'])

    def test_get_author(self):
        author = Author.objects.create(**self.author_data)
        response = self.client.get(f'/authors/{author.author_id}/')  # Use author_id instead of id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], author.name)

    def test_update_author(self):
    # Create an author instance in the database
        author = Author.objects.create(**self.author_data)

    # Data for the update
        updated_data = {'bio': 'Updated bio'}

    # Perform the PUT request to update the 'bio' field
        response = self.client.put(f'/authors/{author.author_id}/', updated_data, format='json')

    # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Ensure that the 'bio' field is updated
        self.assertEqual(response.data['bio'], updated_data['bio'])

    def test_delete_author(self):
        author = Author.objects.create(**self.author_data)
        response = self.client.delete(f'/authors/{author.author_id}/')  # Use author_id
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
