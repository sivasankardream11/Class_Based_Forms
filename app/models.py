from django.db import models

# Create your models here.
class Employe(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_age=models.IntegerField()

    def __str__(self):
        return self.emp_name