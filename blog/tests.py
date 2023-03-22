from django.test import TestCase
import json

from django.urls import reverse
# Create your tests here.
class comroomAPITests(TestCase):
    def test_list(self):
        url = reverse("schedule")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data),1)
        self.assertContains(response, 'time_table')
