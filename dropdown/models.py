from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class department(models.Model):
    departmentname = models.CharField(max_length=100)
    dlink=models.URLField()
    class Meta:
        ordering = ('departmentname',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def __str__(self):
        return '{}'.format(self.departmentname)


class employee(models.Model):
    deptid = models.ForeignKey(department, on_delete=CASCADE)
    empname = models.CharField(max_length=100)

    class Meta:
        ordering = ('empname',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return '{}'.format(self.empname)