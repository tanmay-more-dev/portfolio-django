from django.db import models
from ckeditor.fields import RichTextField

class BlogCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Blog(models.Model):
    title = models.CharField(max_length=100)
    posted_on = models.DateField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    posted_by = models.CharField(max_length=200)
    content = RichTextField(max_length=3800)
    img = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title