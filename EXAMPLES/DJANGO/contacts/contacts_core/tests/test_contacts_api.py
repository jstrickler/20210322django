from rest_framework.test import APITestCase
from django.urls import reverse
from contacts_core.models import Contact, City

class TestContactsAPI(APITestCase):

    def setUp(self):
        self.invalid_id = "123abc"

        def contact_url(id):
            if id is None:
                args = []
            else:
                args = [id]
            return reverse('contacts:api:contact-detail', args=args)

        self.contact_url = contact_url

        def city_url(id):
            return reverse('contacts:api:city-detail', args=[id])

        self.city_url = city_url

    def test_retrieve_contacts_first_name(self):
        for obj in Contact.objects.all():
            expected = obj.first_name
            url = self.contact_url(obj.id)
            response = self.client.get(url)
            self.assertEqual(expected, response["first_name"])

    def test_invalid_contacts_id_returns_404(self):
        expected = 404
        url = self.contact_url(self.invalid_id)
        response = self.client.get(url)
        self.assertEqual(expected, response.status_code)

    def test_invalid_city_id_returns_404(self):
        expected = 404
        url = self.city_url(self.invalid_id)
        response = self.client.get(url)
        self.assertEqual(expected, response.status_code)

    def test_invalid_contact_id_returns_not_found(self):
        expected_key = "detail"
        expected_value = "Not found."
        url = self.contact_url(self.invalid_id)
        response = self.client.get(url)
        json_result = response.json()
        self.assertIn(expected_key, json_result)
        self.assertEqual(expected_value, json_result[expected_key])

    def test_retrieve_city_name(self):
        for obj in City.objects.all():
            expected = obj.name
            url = self.city_url(obj.id)
            response = self.client.get(url)
            self.assertEqual(expected, response["name"])

