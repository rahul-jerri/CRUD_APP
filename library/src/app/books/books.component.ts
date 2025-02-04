import { Component, OnInit } from '@angular/core';
import { BookService } from './book.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class BooksComponent implements OnInit {
  books: any[] = [];
  authors: any[] = [];
  newBook: any = {
    title: '',
    isbn: '',
    publication_date: '',
    available_copies: 0,
    total_copies: 0,
    author_id: null // Make sure this is author_id
  };
  editingBook: any = null;

  constructor(private bookService: BookService) {}

  ngOnInit(): void {
    this.loadBooks();
    this.loadAuthors();
  }

  loadBooks() {
    this.bookService.getBooks().subscribe(
      (data: any[]) => {
        this.books = data;
      },
      (error: any) => {
        console.error('Error fetching books!', error);
      }
    );
  }

  loadAuthors() {
    this.bookService.getAuthors().subscribe(
      (data: any[]) => {
        this.authors = data;
      },
      (error: any) => {
        console.error('Error fetching authors!', error);
      }
    );
  }

  getAuthorName(authorId: number): string {
    const author = this.authors.find((a) => a.author_id === authorId);
    return author ? author.name : 'Unknown';
  }

  addBook() {
    if (!this.newBook.author_id) {
      console.error('Author ID is required!');
      return;
    }
    console.log('Book Data to be sent:', this.newBook);

    const bookData = {
      title: this.newBook.title,
      isbn: this.newBook.isbn,
      publication_date: this.newBook.publication_date,
      available_copies: this.newBook.available_copies,
      total_copies: this.newBook.total_copies,
      author: this.newBook.author_id // Correctly use author_id here
    };

    console.log('Adding book:', bookData);

    this.bookService.addBook(bookData).subscribe(
      (response: any) => {
        this.books.push(response);
        this.resetNewBook();
      },
      (error: any) => {
        console.error('Error adding book!', error);
      }
    );
  }

  editBook(book: any) {
    this.editingBook = { ...book };
  }

  saveEditedBook() {
    if (this.editingBook) {
      this.bookService.updateBook(this.editingBook.book_id, this.editingBook).subscribe(
        (response: any) => {
          const index = this.books.findIndex((book) => book.book_id === this.editingBook.book_id);
          if (index !== -1) {
            this.books[index] = response;
          }
          this.editingBook = null;
        },
        (error: any) => {
          console.error('Error updating book!', error);
        }
      );
    }
  }

  deleteBook(bookId: number) {
    if (!bookId) {
      console.error('Invalid book ID for deletion');
      return;
    }
    this.bookService.deleteBook(bookId).subscribe(
      (response: any) => {
        this.books = this.books.filter(book => book.book_id !== bookId);
      },
      (error: any) => {
        console.error('Error deleting book!', error);
      }
    );
  }

  resetNewBook() {
    this.newBook = {
      title: '',
      isbn: '',
      publication_date: '', // Keep this as a string, format will be handled
      available_copies: 0,
      total_copies: 0,
      author_id: null
    };
  }
}