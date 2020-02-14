from test_plus.test import TestCase
from django_seed import Seed
from django.urls import reverse
from .models import Contact, Organization
from .serializers import ContactSchema


class DemoTestCase(TestCase):
    def setUp(self):
        seeder = Seed.seeder()
        seeder.add_entity(Organization, 80, {
                'name': lambda x: seeder.faker.company(),
        })
        seeder.add_entity(Contact, 80)
        seeder.execute()

    def test_contacts(self):
        self.get_check_200("demo:dashboard")
        self.get_check_200("demo:contacts")
        self.get_check_200("demo:organizations")

    def test_contact_serializer(self):
        contact_schema = ContactSchema()
        contact = Contact.objects.last()
        s = contact_schema.dump(contact)
        
        self.assertTrue(s["organization_id"], contact.organization.id)


    
