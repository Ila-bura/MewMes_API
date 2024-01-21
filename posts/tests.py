from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='ila', password='pass')


def test_can_list_posts(self):
    """Test if a user can list posts"""
    jody = User.objects.get(username='ila')
    Post.objects.create(owner=ila, title='a title')
    response = self.client.get('/posts/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    print(response.data)
    print(len(response.data))


def test_logged_in_user_can_create_post(self):
    """Test if logged in user can create a post"""
    self.client.login(username='ila', password='pass')
    response = self.client.post('/posts/', {'title': 'a title'})
    count = Post.objects.count()
    self.assertEqual(count, 1)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


def test_user_not_logged_in_cant_create_post(self):
    """Test if a logged out user cannot create a post"""
    response = self.client.post('/posts/', {'title': 'a title'})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        ila = User.objects.create_user(username='ila', password='pass')
        misty = User.objects.create_user(username='misty', password='pass')
        Post.objects.create(
            owner=ila, title='a title', content='ilas content'
        )
        Post.objects.create(
            owner=misty, title='another title', content='mistys content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        """Test if a user can retrieve a post using valid ID"""
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        """Test if a user cannot retrieve a post using invalid ID"""
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """Test if a user can update their own posts"""
        self.client.login(username='ila', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """Test if a user cannot update another user's posts"""
        self.client.login(username='misty', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
