from django.db import models

# Create your models here.


class registering(models.Model):
    name = models.CharField(max_length = 20)
    Age = models.IntegerField()
    ide = models.IntegerField()
    collage_name = models.CharField(max_length =50)
    field = models.CharField(max_length =50)
    location = models.CharField(max_length =50)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name



class posting(models.Model):
    name = models.ForeignKey(registering, on_delete=models.CASCADE)
    dis = models.CharField(max_length = 90)
    sub = models.CharField(max_length =50)
    img = models.ImageField(upload_to='img', blank=True, null=True)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.sub


