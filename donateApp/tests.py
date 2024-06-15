from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Event

User = get_user_model()
# Create your tests here.

class EventModelTest(TestCase):
    
    def setUp(self):
        test_user1 = User.objects.create_user(username='tester1', password='EmamDiin')
        
    def test_slug_field_unique(self):
        event1 = Event.objects.create(admin=test_user1, title='Test event', description='described')
        event2 = Event.objects.create(admin=test_user1, title='Test event', description='described two')
        self.assertTrue()
