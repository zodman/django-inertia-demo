from django.db import models


class EntityMix(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state= models.CharField(max_length=100)

    class Meta:
        abstract = True


class Organization(EntityMix):
    name = models.CharField(max_length=100)

    

class Contact(EntityMix):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="contacts")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


