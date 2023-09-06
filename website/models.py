from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField(max_length=700, blank=False)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.name