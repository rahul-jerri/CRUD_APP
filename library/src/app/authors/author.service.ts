import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthorService {
  private apiUrl = 'http://localhost:8000/authors';

  constructor(private http: HttpClient) {}

  getAuthors(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`);
  }

  addAuthor(authorData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, authorData);
  }

  updateAuthor(authorId: number, authorData: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${authorId}/`, authorData);
  }

  deleteAuthor(authorId: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${authorId}/`);
  }
}
