from django.db import models

# Create your models here.
class Sample(models.Model):
    droll = models.CharField(default = "hello" ,max_length = 50)
    rating = models.FloatField(default = 2.3)
    review = models.IntegerField(default = 5)

    def __str__(self):
            return f'droll is :- {self.droll}'