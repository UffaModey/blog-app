import os
import contentful
#from django.db import models

# Create your models here.

client = contentful.Client(
    os.environ.get('CTF_SPACE_ID'),
    os.environ.get('CTF_DELIVERY_KEY')
)