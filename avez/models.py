from django.db import models

# Create your models here.
class Paloma(models.Model):
    edad = models.IntegerField(null=True)
    color = models.CharField(max_length=50)
    habitad = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk} - {self.color}'

    class Meta:
        db_table = 'palomas'


    def migrar(self):
        return 'La paloma se fue a migrar'
    