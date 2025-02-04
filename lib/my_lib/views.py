from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    AuthorSerializer, 
    BookSerializer, 
    BorrowerSerializer, 
    BorrowRecordSerializer
)
from . models import Author, Borrower
from .services.implement import AuthorService, BookService, BorrowRecordService, BorrowerService

# -------------------- AUTHOR VIEWS --------------------
class AuthorListCreateView(APIView):
    service = AuthorService()

    def get(self, request):
        authors = self.service.list_authors()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            author = self.service.create_author(serializer.validated_data)
            return Response(AuthorSerializer(author).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailView(APIView):
    service = AuthorService()

    def get(self, request, author_id):
        try:
            author = self.service.get_author(author_id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, author_id):
        try:
            author = self.service.get_author(author_id)  # Fetch the author from the database
            serializer = AuthorSerializer(author, data=request.data, partial=True)  # partial=True allows partial updates

            if serializer.is_valid():
                updated_author = self.service.update_author(author_id, serializer.validated_data)
                return Response(AuthorSerializer(updated_author).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, author_id):
        try:
            self.service.delete_author(author_id)
            return Response({"message": "Author deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)


# -------------------- BOOK VIEWS --------------------
class BookListCreateView(APIView):
    service = BookService()

    def get(self, request):
        query = request.query_params.get('search', None)
        books = self.service.search_books(query) if query else self.service.dao.get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = self.service.dao.create_book(serializer.validated_data)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    service = BookService()

    def get(self, request, book_id):
        book = self.service.dao.get_book_by_id(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        book = self.service.dao.get_book_by_id(book_id)
        data = request.data.copy()
        # Exclude isbn if you don't want to update it
        data.pop('isbn', None)

        serializer = BookSerializer(data=data, partial=True)
        if serializer.is_valid():
            book = self.service.dao.update_book(book_id, serializer.validated_data)
            return Response(BookSerializer(book).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        self.service.dao.delete_book(book_id)
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class OverdueBooksView(APIView):
    service = BookService()

    def get(self, request):
        overdue_books = self.service.filter_overdue_books()
        serializer = BookSerializer(overdue_books, many=True)
        return Response(serializer.data)


# -------------------- BORROWER VIEWS --------------------
class BorrowerListCreateView(APIView):
    service = BorrowerService()

    def get(self, request):
        borrowers = self.service.dao.get_all_borrowers()
        serializer = BorrowerSerializer(borrowers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BorrowerSerializer(data=request.data)
        if serializer.is_valid():
            borrower = self.service.dao.create_borrower(serializer.validated_data)
            return Response(BorrowerSerializer(borrower).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BorrowerDetailView(APIView):
    service = BorrowerService()

    def get(self, request, borrower_id):
        borrower = self.service.dao.get_borrower_by_id(borrower_id)
        serializer = BorrowerSerializer(borrower)
        return Response(serializer.data)

    def put(self, request, borrower_id):
        try:
            # Get the existing borrower instance
            borrower = Borrower.objects.get(pk=borrower_id)
        except Borrower.DoesNotExist:
            return Response({"error": "Borrower not found."}, status=status.HTTP_404_NOT_FOUND)

        # Pass the existing instance to the serializer
        serializer = BorrowerSerializer(borrower, data=request.data, partial=True)
        if serializer.is_valid():
            # Update the borrower with validated data
            updated_borrower = serializer.save()
            return Response(BorrowerSerializer(updated_borrower).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, borrower_id):
        self.service.dao.delete_borrower(borrower_id)
        return Response({"message": "Borrower deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# -------------------- BORROW RECORD VIEWS --------------------
class BorrowRecordListCreateView(APIView):
    service = BorrowRecordService()

    def get(self, request):
        borrow_records = self.service.dao.get_all_borrow_records()
        serializer = BorrowRecordSerializer(borrow_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BorrowRecordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                borrow_record = self.service.borrow_book(serializer.validated_data)
                return Response(BorrowRecordSerializer(borrow_record).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BorrowRecordDetailView(APIView):
    service = BorrowRecordService()

    def get(self, request, record_id):
        borrow_record = self.service.dao.get_borrow_record_by_id(record_id)
        serializer = BorrowRecordSerializer(borrow_record)
        return Response(serializer.data)

    def put(self, request, record_id):
        return_date = request.data.get('return_date')  # Get the return date from the request
        serializer = BorrowRecordSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            self.service.return_book(record_id, return_date)  # Pass the return date to the service
            return Response({"message": "Book returned successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, record_id):
        self.service.dao.delete_borrow_record(record_id)
        return Response({"message": "Borrow record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
