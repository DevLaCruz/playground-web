from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread,Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1=User.objects.create_user('user1',None,'test1234')
        self.user2=User.objects.create_user('user2',None,'test1234')

        self.thread=Thread.objects.create()

    def add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        threads=Thread.objects.all()
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_thread
