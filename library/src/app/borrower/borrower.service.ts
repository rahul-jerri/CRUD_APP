import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BorrowerService {
  private apiUrl = 'http://127.0.0.1:8000/borrowers/';

  constructor(private http: HttpClient) {}

  getBorrowers(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
  getBorrowerById(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}${id}`);
  }
  addBorrower(borrowerData: any): Observable<any> {
    console.log('Payload being sent to backend:', JSON.stringify(borrowerData));
    return this.http.post<any>(`${this.apiUrl}`, borrowerData);
  }

  updateBorrower(borrowerId: number, borrowerData: any): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });
    return this.http.put<any>(`${this.apiUrl}${borrowerId}/`, borrowerData, { headers: headers });
  }

  deleteBorrower(borrowerId: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}${borrowerId}/`);
  }
}
