from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stars = models.IntegerField()
    review = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.review}   [[[[{self.stars}]]]]"