import { Component, OnInit } from '@angular/core';
import { BorrowRecordService } from './borrow-record.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChangeDetectorRef } from '@angular/core';
import { BookService } from '../books/book.service';  
import { BorrowerService } from '../borrower/borrower.service';  

@Component({
  selector: 'app-borrow-records',
  templateUrl: './borrower-record.component.html',
  styleUrls: ['./borrower-record.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class BorrowRecordsComponent implements OnInit {
  borrowRecords: any[] = [];
  newBorrowRecord: any = {
    book: null,
    borrower: null,
    borrow_date: '',
    return_date: '',
    status: 'borrowed'
  };
  editingBorrowRecord: any = null;

  constructor(private borrowRecordService: BorrowRecordService,
    private Bookservice:BookService,
    private borrowerservice: BorrowerService,
    private cdRef:ChangeDetectorRef) {}

  ngOnInit(): void {
    this.loadBorrowRecords();
  }

  loadBorrowRecords() {
    this.borrowRecordService.getBorrowRecords().subscribe(
      (data: any[]) => {
        this.borrowRecords = data;
      },
      (error: any) => {
        console.error('Error fetching borrow records!', error);
      }
    );
  }

  addBorrowRecord() {
    if (!this.newBorrowRecord.return_date) {
      // Optionally, you can set the return_date to null if not provided
      this.newBorrowRecord.return_date = null;
    }
  
    console.log('Adding borrow record:', this.newBorrowRecord);
  
    this.borrowRecordService.addBorrowRecord(this.newBorrowRecord).subscribe(
      (response: any) => {
        this.borrowRecords.push(response);
        this.resetNewBorrowRecord();
      },
      (error: any) => {
        console.error('Error adding borrow record!', error);
      }
    );
  }
  

  editBorrowRecord(record: any) {
    this.editingBorrowRecord = { ...record };
  }

  saveEditedBorrowRecord() {
    if (this.editingBorrowRecord) {
      this.borrowRecordService.updateBorrowRecord(this.editingBorrowRecord.id, this.editingBorrowRecord).subscribe(
        (response: any) => {
          console.log('updated borrow record:', response);
          const index = this.borrowRecords.findIndex((r) => r.id === this.editingBorrowRecord.id);
          if (index !== -1) {
            this.borrowRecords[index] = response;
          }
          this.editingBorrowRecord = null;
          
          // Trigger change detection manually
          this.cdRef.detectChanges();
        },
        (error: any) => {
          console.error('Error updating borrow record!', error);
        }
      );
    }
  }

  deleteBorrowRecord(recordId: number) {
    this.borrowRecordService.deleteBorrowRecord(recordId).subscribe(
      (response: any) => {
        this.borrowRecords = this.borrowRecords.filter((record) => record.id !== recordId);
      },
      (error: any) => {
        console.error('Error deleting borrow record!', error);
      }
    );
  }

  resetNewBorrowRecord() {
    this.newBorrowRecord = {
      book: null,
      borrower: null,
      borrow_date: '',
      return_date: '',
      status: 'borrowed'
    };
  }
}
