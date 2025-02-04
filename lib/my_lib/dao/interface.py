from abc import ABC, abstractmethod
from typing import List
from ..models import Book,BorrowRecord
class AuthorDAOInterface(ABC):
    @abstractmethod
    def get_all_authors(self):
        pass

    @abstractmethod
    def get_author_by_id(self, author_id):
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

class BookDAOInterface(ABC):
    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def get_book_by_id(self, book_id):
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
    def get_books_by_title_or_author(self, search_term: str) -> List[Book]:
        pass

class BorrowerDAOInterface(ABC):
    @abstractmethod
    def get_all_borrowers(self):
        pass

    @abstractmethod
    def get_borrower_by_id(self, borrower_id):
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

class BorrowRecordDAOInterface(ABC):
    @abstractmethod
    def get_all_borrow_records(self):
        pass

    @abstractmethod
    def get_borrow_record_by_id(self, record_id):
        pass

    @abstractmethod
    def create_borrow_record(self, data):
        pass

    @abstractmethod
    def update_borrow_record(self, record_id, data):
        pass

    @abstractmethod
    def delete_borrow_record(self, record_id):
        pass
    @abstractmethod
    def get_overdue_books(self) -> List[BorrowRecord]:
        pass

