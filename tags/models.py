from django.db import models
from authors.baseModel import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
