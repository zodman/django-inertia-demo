from django.test import TestCase
from django.test import Client
from django_seed import Seed
from django.urls import reverse
from .models import Contact, Organization


class DemoTestCase(TestCase):
    def setUp(self):
        seeder = Seed.seeder()
        seeder.add_entity(Organization, 80, {
                'name': lambda x: fake.faker.company(),
        })
        seeder.add_entity(Contact, 80)

    def test_contacts(self):
        self.client = Client()
        response = self.client.get(reverse("demo:contacts"))
        self.assertEqual(200, response.status_code)

    