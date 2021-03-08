from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index-template.html', {
        'books': books
    })

# for adding a new book


def create_book(request):
    if request.method == 'POST':
        create_form = BookForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        pass
    else:
        create_form = BookForm()
        return render(request, 'books/create-template.html', {
            'form': create_form
        })

# updating


def update_book(request, book_id):
    if request.method == "POST":
        book_being_changed = get_object_or_404(Book, pk=book_id)
        book_form = BookForm(request.POST, instance=book_being_changed)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
    else:
        book_being_changed = get_object_or_404(Book, pk=book_id)
        book_form = BookForm(instance=book_being_changed)
    return render(request, 'books/update-template.html', {
        'form': book_form
    })
