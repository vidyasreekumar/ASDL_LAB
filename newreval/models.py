from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

class Class(models.Model):
    class_id = models.CharField(max_length=4)
    class_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('class_id',)
        verbose_name_plural = "Class"


    def __str__(self):
        return str(self.class_id)


class UserDetails(models.Model):
    ktu_id = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key= True , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    #approved_date = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('ktu_id',)
        verbose_name_plural = "UserDetails"


    def __str__(self):
        return str(self.ktu_id)

class Sem(models.Model):
    sem_id = models.IntegerField(primary_key= True)
    sem_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('sem_id',)
        verbose_name_plural = "Semesters"


    def __str__(self):
        return str(self.sem_id)
class Subjects(models.Model):
    sub_id = models.CharField(primary_key= True, max_length=4)
    sub_name = models.CharField(max_length=20)
    sem_id = models.ForeignKey(Sem, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    fees = models.IntegerField()

    class Meta:
        ordering = ('sub_id',)
        verbose_name_plural = "Subjects"


    def __str__(self):
        return str(self.sub_id)



class Reval(models.Model):
    date = models.DateField(default=datetime.now)
    ktu_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    paid = models.BooleanField(default=False)
    fees = models.IntegerField()
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    class Meta:
        ordering = ('ktu_id',)
        verbose_name_plural = "NewRevaluation"

    def __str__(self):
        return str(self.ktu_id)
