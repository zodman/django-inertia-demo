from test_plus.test import TestCase
from django_seed import Seed
from django.urls import reverse
from .models import Contact, Organization
from .serializers import ContactSchema, OrganizationSchema


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

    def test_org_serializer(self):
        org_schema = OrganizationSchema()
        org = Organization.objects.last()
        r = org_schema.dump(org)
        self.assertTrue( "contacts" in r, r)
        self.assertTrue(len(r["contacts"])>0)

    def __test_flash(self):
        contact = Contact.objects.last()
        self.get_check_200("demo:contact.edit", id=contact.id)
        self.delete("demo:contact.edit", id=contact.id)
        self.response_301()
