from django.urls import path
from .views import HomePageView, BookListView
# from .views import 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('book/', BookListView.as_view(), name='book_list'),
]
