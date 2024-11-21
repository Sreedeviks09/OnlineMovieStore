from django.db import models

# Create your models here.
class MovieStore(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)

    def __str__(self):
        return self.title