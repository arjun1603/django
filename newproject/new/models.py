from django.db import models

# Create your models here.

class Task(models.Model):

    task_name = models.CharField(max_length=200, default=1)
    task_desc = models.CharField(max_length=200, default=1)
    date_created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/',default="Image/None/Noimg.jp")


class Employee (models.Model):
    cid = models.IntegerField()
    ename = models.CharField(max_length=50)
    esalary = models.FloatField()

    def __str__(self):
        return f"{self.cid}--{self.ename}"
