import { Routes } from '@angular/router';
import { AuthorsComponent } from './authors/authors.component';
import { BooksComponent } from './books/books.component';
import { BorrowersComponent } from './borrower/borrower.component';
import { BorrowRecordsComponent } from './borrower-record/borrower-record.component';

export const routes: Routes = [
    {path: '', redirectTo: 'authors', pathMatch: 'full'},
    { path: 'authors', component: AuthorsComponent },
    {path:'books',component:BooksComponent},  
    {path:'borrowers',component:BorrowersComponent},
    {path:'borrower-record',component:BorrowRecordsComponent}, 
    { path: '**', redirectTo: 'authors' }
 
];
