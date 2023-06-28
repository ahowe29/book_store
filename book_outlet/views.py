from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg

from .models import Book


def index(request):
    books = Book.objects.all().order_by("title")  # -rating would be descending
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except ObjectDoesNotExist:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html", {
        "title": book.title,
        "rating": book.rating,
        "is_best_selling_book": book.is_best_selling_book,
        "author": book.author,
    })
