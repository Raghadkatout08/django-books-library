from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Book

class HomeViewTest(TestCase):
    
    def test_home_view(self):
        url = reverse('home')  
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'home.html')
        
        self.assertContains(response, '<h1>Welcome to the Library Home Page</h1>')
        self.assertContains(response, 'View Books')
        
class BookListViewTest(TestCase):
    
    def setUp(self):
        self.User = get_user_model()
        self.user1 = self.User.objects.create_user(username='testuser', password='password123')
        
        Book.objects.create(
            auther=self.user1,
            title='To Kill a Mockingbird',
            description='A novel by Harper Lee.',
            rating=5,
            publish_date='1960-07-11'
        )
        Book.objects.create(
            auther=self.user1,
            title='1984',
            description='A dystopian novel by George Orwell.',
            rating=4,
            publish_date='1949-06-08'
        )
    
    def test_book_list_view(self):
        url = reverse('book_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertContains(response, '<h1> Book List </h1>')
        self.assertContains(response, 'Author Name: {}'.format(self.user1.username))
        self.assertContains(response, 'Title: To Kill a Mockingbird')
        self.assertContains(response, 'Description: A novel by Harper Lee.')
        self.assertContains(response, 'Rating: 5')
        self.assertContains(response, 'Publish Date: July 11, 1960')