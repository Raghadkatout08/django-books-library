from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.book = Book.objects.create(
            auther=self.user,
            title='Test Book',
            description='Test Description',
            rating=5,
            publish_date='2023-01-01'
        )

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_book_list_view_status_code(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertTemplateUsed(response, 'book_list.html')

    def test_book_list_view_context(self):
        response = self.client.get(reverse('book_list'))
        self.assertTrue('books_object' in response.context)
        self.assertEqual(len(response.context['books_object']), 1)
        self.assertEqual(response.context['books_object'][0].title, 'Test Book')

    def test_book_details_view_status_code(self):
        response = self.client.get(reverse('details_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_details_view_template(self):
        response = self.client.get(reverse('details_book', args=[self.book.id]))
        self.assertTemplateUsed(response, 'details_book.html')

    def test_book_details_view_context(self):
        response = self.client.get(reverse('details_book', args=[self.book.id]))
        self.assertTrue('book' in response.context)
        self.assertEqual(response.context['book'].title, 'Test Book')
