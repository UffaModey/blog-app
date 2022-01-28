import os
import contentful
from django.db import models

# Create your models here.

client = contentful.Client(
    os.environ.get('CTF_SPACE_ID'),
    os.environ.get('CTF_DELIVERY_KEY')
)

class Emails(models.Model):
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.email