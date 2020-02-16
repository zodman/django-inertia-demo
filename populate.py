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
args = {
    'country': lambda x: fake.faker.random_element(elements=('CA', 'US')),
    'region': lambda x:fake.faker.state(),
    'address': lambda x:fake.faker.address().replace("\n"," "),
    'postal_code': lambda x:fake.faker.postalcode(),
}
org_args = args.copy()
org_args.update({
    'name': lambda x: fake.faker.company(),
})
fake.add_entity(Organization, 80,org_args) 
fake.add_entity(Contact, 80, args)

print("execute")
fake.execute()
