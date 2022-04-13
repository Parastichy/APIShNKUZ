from django.db import models


# Create your models here.
from django.urls import reverse


class Standard(models.Model):
    searchCode = models.CharField(max_length=20, unique=True, verbose_name='Шифр поисковый (уникальный)')
    originalCipherFromDocument = models.CharField(max_length=128, verbose_name='Оригинальный шифр с документа')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    unit = models.CharField(max_length=64, verbose_name='Единица измерения')


    def get_absolute_url(self):
        return reverse('get_standard', kwargs={'searchCode': self.searchCode})


    def my_func(self):
        return f'Hello {self.originalCipherFromDocument}'

    def __str__(self):
        return self.searchCode


class ResourceRequirement(models.Model):
    standard = models.ForeignKey('Standard', null=True, blank=True, on_delete=models.CASCADE, related_name='must')
    expenditure = models.ForeignKey('Resources', null=True, blank=True, on_delete=models.CASCADE)
    consumptionRate = models.FloatField(verbose_name='Норма расхода ')

    def __str__(self):
        return f"{self.expenditure}"


class Resources(models.Model):
    code = models.IntegerField(verbose_name='Код')
    resourceName = models.CharField(max_length=255, verbose_name='Наименование ресурса (полное)')
    unit = models.ForeignKey('Unit', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Единица измерения')

    def __str__(self):
        return f"{self.resourceName}"


class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Единица измерения')
    denominator = models.IntegerField(verbose_name='Делитель')

    def __str__(self):
        return f"{self.name}"
