from test_plus.test import TestCase
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
        self.get_check_200("demo:dashboard")
        self.get_check_200("demo:contacts")
        self.get_check_200("demo:organizations")

    
