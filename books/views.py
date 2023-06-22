from django.shortcuts import render, redirect
from .models import Book
from stdnum import isbn

from isbnlib import  is_isbn10, is_isbn13


def landing_page(request):
    books = Book.objects.all()
    return render(request, 'books/landing_page.html', {'books': books})

def isbn_verify(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        if is_isbn10(isbn) or is_isbn13(isbn):
            return render(request, 'books/isbn_verify.html', {'valid': True})
        else:
            return render(request, 'books/isbn_verify.html', {'valid': False})
    return render(request, 'books/isbn_verify.html')









def scan_book(request):
    if request.method == 'POST':
        scanned_isbn = request.POST['isbn']
        book_data = isbn.get_book_data(scanned_isbn)
        title = book_data.get('title', '')
        author = book_data.get('author', '')
        publisher = book_data.get('publisher', '')
        publication_date = book_data.get('publication_date', '')
        edition = book_data.get('edition', '')
        description = book_data.get('description', '')
        price = book_data.get('price', '')
        language = book_data.get('language', '')

        book = Book(
            title=title,
            author=author,
            publisher=publisher,
            publication_date=publication_date,
            edition=edition,
            description=description,
            price=price,
            language=language,
            isbn=scanned_isbn
        )
        book.save()
        return redirect('book_list')
    
    return render(request, 'books/scan_book.html')
