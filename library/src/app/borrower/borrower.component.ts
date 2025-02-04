import { Component, OnInit } from '@angular/core';
import { BorrowerService } from './borrower.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-borrowers',
  templateUrl: './borrower.component.html',
  styleUrls: ['./borrower.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class BorrowersComponent implements OnInit {
  borrowers: any[] = [];
  newBorrower: any = {
    name: '',
    email: '',
    phone_number: '',
    membership_date: '' // Expected as a string (e.g., "2025-01-01")
  };
  editingBorrower: any = null;

  constructor(private borrowerService: BorrowerService) {}

  ngOnInit(): void {
    this.loadBorrowers();
  }

  loadBorrowers(): void {
    this.borrowerService.getBorrowers().subscribe(
      (data: any[]) => {
        this.borrowers = data;
      },
      (error: any) => {
        console.error('Error fetching borrowers!', error);
      }
    );
  }

  addBorrower(): void {
    console.log('Adding borrower (payload):', JSON.stringify(this.newBorrower));
  
    this.borrowerService.addBorrower(this.newBorrower).subscribe(
      (response: any) => {
        console.log('Borrower added successfully:', response);
        this.borrowers.push(response);
        this.resetNewBorrower();
      },
      (error: any) => {
        console.error('Error adding borrower:', error.error);
      }
    );
  }
  
  

  editBorrower(borrower: any): void {
    this.editingBorrower = { ...borrower };
  }

  saveEditedBorrower(): void {
    if (this.editingBorrower) {
      this.borrowerService.updateBorrower(this.editingBorrower.id, this.editingBorrower).subscribe(
        (response: any) => {
          const index = this.borrowers.findIndex((b) => b.id === this.editingBorrower.id);
          if (index !== -1) {
            this.borrowers[index] = response;
          }
          this.editingBorrower = null;
        },
        (error: any) => {
          console.error('Error updating borrower!', error);
        }
      );
    }
  }

  deleteBorrower(borrowerId: number): void {
    this.borrowerService.deleteBorrower(borrowerId).subscribe(
      (response: any) => {
        this.borrowers = this.borrowers.filter((borrower) => borrower.id !== borrowerId);
      },
      (error: any) => {
        console.error('Error deleting borrower!', error);
      }
    );
  }

  resetNewBorrower(): void {
    this.newBorrower = {
      name: '',
      email: '',
      phone_number: '',
      membership_date: ''
    };
  }
}
