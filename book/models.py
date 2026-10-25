from core.models import BaseModel
from django.db import models


class Book(BaseModel):
    title = models.CharField(max_length=200)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.title
