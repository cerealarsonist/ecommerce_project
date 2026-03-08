from djongo import models

class Product(models.Model):
    id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    tags = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name