from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Book

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = "books_object"