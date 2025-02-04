from abc import ABC, abstractmethod
from ..models import Book,BorrowRecord
from typing import List
class AuthorServiceInterface(ABC):
    @abstractmethod
    def list_authors(self):
        pass

    @abstractmethod
    def get_author(self, author_id):
        pass

    @abstractmethod
    def create_author(self, data):
        pass

    @abstractmethod
    def update_author(self, author_id, data):
        pass

    @abstractmethod
    def delete_author(self, author_id):
        pass

class BookServiceInterface(ABC):
    @abstractmethod
    def list_books(self):
        pass

    @abstractmethod
    def get_book(self, book_id):
        pass

    @abstractmethod
    def create_book(self, data):
        pass

    @abstractmethod
    def update_book(self, book_id, data):
        pass

    @abstractmethod
    def delete_book(self, book_id):
        pass

    @abstractmethod
    def search_books(self, query):
        pass

    @abstractmethod
    def filter_overdue_books(self):
        pass
    @abstractmethod
    def search_books1(self, search_term: str) -> List[Book]:
        pass

class BorrowerServiceInterface(ABC):
    @abstractmethod
    def list_borrowers(self):
        pass

    @abstractmethod
    def get_borrower(self, borrower_id):
        pass

    @abstractmethod
    def create_borrower(self, data):
        pass

    @abstractmethod
    def update_borrower(self, borrower_id, data):
        pass

    @abstractmethod
    def delete_borrower(self, borrower_id):
        pass

class BorrowRecordServiceInterface(ABC):
    @abstractmethod
    def list_borrow_records(self):
        pass

    @abstractmethod
    def get_borrow_record(self, record_id):
        pass

    @abstractmethod
    def borrow_book(self, data):
        pass

    @abstractmethod
    def return_book(self, record_id):
        pass
    @abstractmethod
    def get_overdue_books(self) -> List[BorrowRecord]:
        pass