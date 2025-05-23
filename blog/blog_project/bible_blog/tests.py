from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
  def set_up(self):
    self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret')
    self.post = Post.objects.create(title='A good title', body='Nice body content', author=self.user)

  def test_string_representation(self):
    post = Post(title='A simple title')
    self.assertEqual(str(post), post.title)

  def test_post_content(self):
    self.assertEqual(f"{self.user.title}", "A good title")
    self.assertEqual(f'{self.user.author}', 'testuser')
    self.assertEqual(f'{self.user.body}', 'Nice body content')

  def test_post_list_view(self): # for BlogListView
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice body content')
    self.assertTemplateUsed(response, 'home.html')

  def test_post_detail_view(self): # for BlogDetailview
    response = self.client.get('post/1/')
    no_response = self.client.get('post/100000')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'A good title')
    self.assertTemplateUsed(response, 'post_detail.html')

  def test_post_create_view(self): # for BlogCreateView
    response = self.client.post(reverse('post_new'), {'title': 'New title', 'author': self.user, 'body': 'New text'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "New title")
    self.assertContains(response, "New text")

  def test_post_update_view(self): # for BlogUpdateView
    response = self.client.post(reverse('post_edit', args=1), {'title': 'Updated title', 'body': 'Updated text'})
    self.assertEqual(response.status_code, 302)

  def test_post_delete_view(self):
    response = self.client.get(reverse('post_delete', args=1))
    self.assertEqual(response.status_code, 200)