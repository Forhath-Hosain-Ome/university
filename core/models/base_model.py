from django.db import models

class basemodel(models.Model):
    is_active = models.BooleanField( default=True )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )