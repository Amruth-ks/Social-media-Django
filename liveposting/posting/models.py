from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="species_images/", blank=True, null=True)
    description = models.CharField(max_length=120)
    cash_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
