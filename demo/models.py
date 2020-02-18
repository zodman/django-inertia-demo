from django.db import models




class EntityMix(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    region= models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=25)
    deleted = models.BooleanField(default=False)



    class Meta:
        abstract = True


class Organization(EntityMix):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)



class Contact(EntityMix):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="contacts")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ("first_name", "last_name")
        
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


