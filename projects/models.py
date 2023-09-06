from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=100)
    url = models.URLField(max_length=500)
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
    