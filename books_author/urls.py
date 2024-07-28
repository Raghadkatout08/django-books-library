from django.urls import path
from .views import HomePageView, BookListView, BookDetailsView
# from .views import 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('details_book/<int:pk>/', BookDetailsView.as_view(), name='details_book'),
]
