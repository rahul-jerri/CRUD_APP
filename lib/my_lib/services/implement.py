from .interface import AuthorServiceInterface, BookServiceInterface, BorrowerServiceInterface, BorrowRecordServiceInterface
from ..dao.implement import AuthorDAO, BookDAO, BorrowerDAO, BorrowRecordDAO
from datetime import date
from ..models import Book,BorrowRecord
from typing import List

class AuthorService(AuthorServiceInterface):
    def __init__(self):
        self.dao = AuthorDAO()

    def list_authors(self):
        return self.dao.get_all_authors()

    def get_author(self, author_id):
        return self.dao.get_author_by_id(author_id)

    def create_author(self, data):
        return self.dao.create_author(data)

    def update_author(self, author_id, data):
        return self.dao.update_author(author_id, data)

    def delete_author(self, author_id):
        return self.dao.delete_author(author_id)

class BookService(BookServiceInterface):
    def __init__(self):
        self.dao = BookDAO()

    def list_books(self):
        return self.dao.get_all_books()

    def get_book(self, book_id):
        return self.dao.get_book_by_id(book_id)

    def create_book(self, data):
        return self.dao.create_book(data)

    def update_book(self, book_id, data):
        return self.dao.update_book(book_id, data)

    def delete_book(self, book_id):
        return self.dao.delete_book(book_id)

    def search_books(self, query):
        return self.dao.get_all_books().filter(title__icontains=query) 
    def search_books1(self, search_term: str) -> List[Book]:
        # Use the DAO to fetch the books
        book_dao = BookDAO()
        return book_dao.get_books_by_title_or_author(search_term)

    def filter_overdue_books(self):
        return self.dao.get_all_books().filter(borrow_records__return_date__lt=date.today())

class BorrowerService(BorrowerServiceInterface):
    def __init__(self):
        self.dao = BorrowerDAO()

    def list_borrowers(self):
        return self.dao.get_all_borrowers()

    def get_borrower(self, borrower_id):
        return self.dao.get_borrower_by_id(borrower_id)

    def create_borrower(self, data):
        return self.dao.create_borrower(data)

    def update_borrower(self, borrower_id, data):
        return self.dao.update_borrower(borrower_id, data)

    def delete_borrower(self, borrower_id):
        return self.dao.delete_borrower(borrower_id)
    

class BorrowRecordService(BorrowRecordServiceInterface):
    def __init__(self):
        self.dao = BorrowRecordDAO()

    def list_borrow_records(self):
        return self.dao.get_all_borrow_records()

    def get_borrow_record(self, record_id):
        return self.dao.get_borrow_record_by_id(record_id)

    def borrow_book(self, data):
        return self.dao.create_borrow_record(data)

    def return_book(self, record_id, return_date):
        record = self.dao.get_borrow_record_by_id(record_id)
        record.book.available_copies += 1
        record.book.save()

        # Set the return_date provided by the user
        record.return_date = return_date  # The user provides the return date
        record.status = 'returned'
        record.save()
    def get_overdue_books(self) -> List[BorrowRecord]:
        # Use the DAO to fetch the overdue borrow records
        borrow_record_dao = BorrowRecordDAO()
        return borrow_record_dao.get_overdue_books()