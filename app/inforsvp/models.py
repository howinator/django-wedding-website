from django.db import models

# Create your models here.
class RSVP(models.Model):
    name = models.CharField(max_length=5000)
    email = models.EmailField()
    number_attending = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extra_info = models.CharField(max_length=500000)
