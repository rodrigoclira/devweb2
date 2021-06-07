from django.db import models
from core.models import Professor

# Create your models here.
class Tipo(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nome}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500, verbose_name="descrição")
    inicio = models.DateField(verbose_name="início")
    fim = models.DateField(blank=True)
    aprovado = models.BooleanField(default=False, verbose_name="Está institucionalizado?")
    coordenador = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titulo}"

class TipoProjeto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)


class ColaboradorProjeto(models.Model):
    colaborador = models.ForeignKey(Professor, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.tag}"
        
class ProjetoTag(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
