from django.db import models


class News(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title

