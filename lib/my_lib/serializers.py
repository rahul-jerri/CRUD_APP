from rest_framework import serializers
from .models import Author, Book, Borrower, BorrowRecord
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

    def validate_email(self, value):
        if not value.endswith(".com"):
            raise serializers.ValidationError("Email must belong to 'example.com' domain.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'borrower', 'borrow_date', 'return_date', 'status']
        extra_kwargs = {
            'return_date': {'required': False}  # Make return_date optional
        }

    def validate(self, data):
        # Check if return_date is provided and if it's valid
        if 'return_date' in data and data['return_date']:
            # Ensure return_date is not earlier than borrow_date
            borrow_record = self.instance
            if borrow_record and borrow_record.borrow_date:
                if data['return_date'] < borrow_record.borrow_date:
                    raise serializers.ValidationError("Return date cannot be earlier than borrow date.")
        return data

