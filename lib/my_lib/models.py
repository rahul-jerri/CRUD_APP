from django.db import models

# Create your models here.



class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField(null=True,blank=True)
    bio=models.CharField(max_length=1000,blank=True)
    
    # class Meta:
    #     db_table='authors'

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    isbn=models.CharField(max_length=100,unique=True)
    publication_date=models.DateField()
    available_copies=models.IntegerField()
    total_copies=models.PositiveIntegerField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    # class Meta:
    #     db_table="book"

    def __str__(self):
        return self.title

class Borrower(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
   
    email=models.EmailField(max_length=254,unique=True)
    phone_number=models.CharField(max_length=10,unique=True)
    membership_date=models.DateField()

    # class Meta:
    #     db_table='borrowers'


    def __str__(self):
        return self.name

class BorrowRecord(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('late', 'Late'),
    ]
    id=models.AutoField(primary_key=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrow_records')
    borrower=models.ForeignKey(Borrower,on_delete=models.CASCADE,related_name='borrow_records')
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=True)
    def clean(self):
        # Enforce borrow_date <= current date
        from django.core.exceptions import ValidationError
        from datetime import date

        if self.borrow_date > date.today():
            raise ValidationError("Borrow date cannot be in the future.")
        if self.return_date and self.return_date < self.borrow_date:
            raise ValidationError("Return date cannot be earlier than borrow date.")
    
    # db_table='borrow_records'

    def __str__(self):
        return f"{self.borrower.name} borrowed {self.book.title}"