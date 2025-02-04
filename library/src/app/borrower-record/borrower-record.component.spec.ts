import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BorrowerRecordComponent } from './borrower-record.component';

describe('BorrowerRecordComponent', () => {
  let component: BorrowerRecordComponent;
  let fixture: ComponentFixture<BorrowerRecordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BorrowerRecordComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BorrowerRecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
