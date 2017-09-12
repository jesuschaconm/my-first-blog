from django.db import models
from django.utils import timezone

class Persona(models.Model):
    nombre = models.CharField(max_length=250)
    edad = models.IntegerField()
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre

class Post(models.Model):
    author = models.ForeignKey(Persona)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


    
        
