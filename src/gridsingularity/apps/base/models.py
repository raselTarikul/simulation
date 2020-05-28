from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """Abstract model that defines a set of fields which are common to all
    models"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
