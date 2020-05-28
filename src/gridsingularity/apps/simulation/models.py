from django.db import models
from gridsingularity.apps.base.models import BaseModel

# Create your models here.


class SimulationResult(BaseModel):
    """ This Class represent the simulation result """
    active = models.DecimalField(max_digits=5, decimal_places=2)
    reactive = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.active) + ' ' + str(self.reactive)
