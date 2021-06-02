from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    lattes = models.URLField(verbose_name="CV Lattes")

    def __str__(self):
        return f"{self.nome}"
