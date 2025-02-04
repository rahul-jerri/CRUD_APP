import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BorrowRecordService {
  private apiUrl = 'http://localhost:8000/borrow-records';  // Adjust this to your backend API URL

  constructor(private http: HttpClient) {}

  getBorrowRecords(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`);
  }

  addBorrowRecord(borrowRecordData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, borrowRecordData);
  }

  updateBorrowRecord(recordId: number, borrowRecordData: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${recordId}/`, borrowRecordData);
  }

  deleteBorrowRecord(recordId: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${recordId}/`);
  }
}
