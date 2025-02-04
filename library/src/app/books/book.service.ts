import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private apiUrl = 'http://localhost:8000/books';

  constructor(private http: HttpClient) {}

  getBooks(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`);
  }

  getAuthors(): Observable<any[]> {
    return this.http.get<any[]>('http://127.0.0.1:8000/authors/');
  }
  getBookById(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/${id}`);
  }

  addBook(bookData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, bookData);
  }

  updateBook(bookId: number, bookData: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${bookId}/`, bookData);
  }

  deleteBook(bookId: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${bookId}/`);
  }
}