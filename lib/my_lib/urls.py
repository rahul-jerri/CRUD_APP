from django.urls import path,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
 
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management System API",
        default_version='v1',
        description="API documentation for the Library Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
 

from .views import (
    AuthorListCreateView, AuthorDetailView,
    BookListCreateView, BookDetailView, OverdueBooksView,
    BorrowerListCreateView, BorrowerDetailView,
    BorrowRecordListCreateView, BorrowRecordDetailView
)

urlpatterns = [
    # Author routes
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name='author-detail'),

    # Book routes
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/overdue/', OverdueBooksView.as_view(), name='overdue-books'),

    # Borrower routes
    path('borrowers/', BorrowerListCreateView.as_view(), name='borrower-list-create'),
    path('borrowers/<int:borrower_id>/', BorrowerDetailView.as_view(), name='borrower-detail'),

    # Borrow Record routes
    path('borrow-records/', BorrowRecordListCreateView.as_view(), name='borrow-record-list-create'),
    path('borrow-records/<int:record_id>/', BorrowRecordDetailView.as_view(), name='borrow-record-detail'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
