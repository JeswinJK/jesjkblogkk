from django.db import models
class student(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()
    Phoneno=models.IntegerField()

# Create your models here.


# Create your models here.
