from ..models import Author, Book, Borrower, BorrowRecord
from typing import List,Dict
from datetime import date
class AuthorDAO:
    def get_all_authors(self):
        return Author.objects.all()

    def get_author_by_id(self, author_id):
        return Author.objects.get(pk=author_id)

    def create_author(self, data):
        return Author.objects.create(**data)

    def update_author(self, author_id, data):
        Author.objects.filter(pk=author_id).update(**data)

    def delete_author(self, author_id):
        Author.objects.filter(pk=author_id).delete()

class BookDAO:
    def get_all_books(self) -> List[Book]:
        """
        Get all books, including the author details using select_related.
        """
        return Book.objects.select_related('author').all()

    def get_book_by_id(self, book_id: int) -> Book:
        """
        Get a specific book by its ID.
        """
        return Book.objects.get(pk=book_id)

    def create_book(self, data: Dict) -> Book:
        """
        Create a new book record.
        """
        return Book.objects.create(**data)

    def update_book(self, book_id: int, data: Dict) -> Book:
        """
        Update an existing book record.
        """
        book = Book.objects.get(pk=book_id)
        for key, value in data.items():
            setattr(book, key, value)
        book.save()
        return book
 

        Book.objects.filter(pk=book_id).update(**data)

    def delete_book(self, book_id: int) -> None:
        """
        Delete a book record by its ID.
        """
        Book.objects.filter(pk=book_id).delete()

    def get_books_by_title_or_author(self, search_term: str) -> List[Book]:
        """
        Search for books by title or author's name.
        """
        return Book.objects.filter(
            title__icontains=search_term
        ) | Book.objects.filter(
            author__name__icontains=search_term
        )
class BorrowerDAO:
    def get_all_borrowers(self):
        return Borrower.objects.all()

    def get_borrower_by_id(self, borrower_id):
        return Borrower.objects.get(pk=borrower_id)

    def create_borrower(self, data):
        return Borrower.objects.create(**data)

    def update_borrower(self, borrower_id, data):
        Borrower.objects.filter(pk=borrower_id).update(**data)


    def delete_borrower(self, borrower_id):
        Borrower.objects.filter(pk=borrower_id).delete()

class BorrowRecordDAO:
    def get_all_borrow_records(self) -> List[BorrowRecord]:
        """
        Get all borrow records, including related book and borrower details using select_related.
        """
        return BorrowRecord.objects.select_related('book', 'borrower').all()

    def get_borrow_record_by_id(self, record_id: int) -> BorrowRecord:
        """
        Get a specific borrow record by its ID.
        """
        return BorrowRecord.objects.get(pk=record_id)

    def create_borrow_record(self, data: Dict) -> BorrowRecord:
        """
        Create a new borrow record. Ensures there are available copies of the book.
        """
        book = data['book']
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()
            return BorrowRecord.objects.create(**data)
        raise ValueError("No copies available.")

    def update_borrow_record(self, record_id: int, data: Dict) -> None:
        """
        Update an existing borrow record.
        """
        BorrowRecord.objects.filter(pk=record_id).update(**data)

    def delete_borrow_record(self, record_id: int) -> None:
        """
        Delete a borrow record by its ID.
        """
        BorrowRecord.objects.filter(pk=record_id).delete()

    def get_overdue_books(self) -> List[BorrowRecord]:
        """
        Fetch all borrow records with a 'borrowed' status and a return date older than today.
        """
        return BorrowRecord.objects.filter(
            return_date__lt=date.today(),
            status='borrowed'
        )
