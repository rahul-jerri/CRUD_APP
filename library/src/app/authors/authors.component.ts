import { Component, OnInit } from '@angular/core';
import { AuthorService } from './author.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class AuthorsComponent implements OnInit {
  authors: any[] = [];
  newAuthor: any = {
    name: '',
    date_of_birth: '',
    bio: ''
  };
  editingAuthor: any = null;
  searchTerm: string = ''; // Added for search functionality

  constructor(private authorService: AuthorService) {}

  ngOnInit(): void {
    this.loadAuthors();
  }

  loadAuthors() {
    this.authorService.getAuthors().subscribe(
      (data: any[]) => {
        this.authors = data;
      },
      (error: any) => {
        console.error('Error fetching authors!', error);
      }
    );
  }

  get filteredAuthors() {
    // Filter authors based on the search term (case-insensitive)
    return this.authors.filter(author =>
      author.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

  addAuthor() {
    if (!this.newAuthor.name || !this.newAuthor.date_of_birth) {
      console.error('Name and Date of Birth are required!');
      return;
    }
    this.authorService.addAuthor(this.newAuthor).subscribe(
      (response: any) => {
        this.authors.push(response);
        this.resetNewAuthor();
      },
      (error: any) => {
        console.error('Error adding author!', error);
      }
    );
  }

  editAuthor(author: any) {
    this.editingAuthor = { ...author };
  }

  saveEditedAuthor() {
    if (this.editingAuthor) {
      this.authorService.updateAuthor(this.editingAuthor.author_id, this.editingAuthor).subscribe(
        (response: any) => {
          const index = this.authors.findIndex((a) => a.author_id === this.editingAuthor.author_id);
          if (index !== -1) {
            this.authors[index] = response;
          }
          this.editingAuthor = null;
        },
        (error: any) => {
          console.error('Error updating author!', error);
        }
      );
    }
  }

  deleteAuthor(authorId: number) {
    this.authorService.deleteAuthor(authorId).subscribe(
      (response: any) => {
        this.authors = this.authors.filter(author => author.author_id !== authorId);
      },
      (error: any) => {
        console.error('Error deleting author!', error);
      }
    );
  }

  resetNewAuthor() {
    this.newAuthor = {
      name: '',
      date_of_birth: '',
      bio: ''
    };
  }
}
