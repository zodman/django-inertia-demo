import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
from django.conf import settings
django.setup()
from django_seed import Seed
from demo.models import Contact, Organization

Contact.objects.all().delete()
Organization.objects.all().delete()

fake = Seed.seeder()

fake.add_entity(Organization, 80, {
    'name': lambda x: fake.faker.company(),
})
fake.add_entity(Contact, 80)

print("execute")
fake.execute()