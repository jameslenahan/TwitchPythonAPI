from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def _str_(self):
        return self.name
