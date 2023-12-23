from django.db import models

class Pro(models.Model):
    Name = models.CharField(max_length=255)
    Custo = models.CharField(max_length = 255)
    Budget = models.IntegerField(null = True)
    year = models.IntegerField(null = True)
    Date_of_completion = models.DateField(null = True)

    def __str__(self):
         return f"{self.Name}"