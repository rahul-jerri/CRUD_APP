import { TestBed } from '@angular/core/testing';

import { BorrowRecordService } from './borrow-record.service';

describe('BorrowRecordService', () => {
  let service: BorrowRecordService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BorrowRecordService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
