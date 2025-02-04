import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BorrowersComponent } from './borrower.component';

describe('BorrowerComponent', () => {
  let component: BorrowersComponent;
  let fixture: ComponentFixture<BorrowersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BorrowersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BorrowersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
