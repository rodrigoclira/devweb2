from django.db import models
from django.db.models.fields import DateTimeField, IntegerField
from core.models import Professor
import mongoengine 
from datetime import datetime

class Comentario(mongoengine.Document):
    projeto = mongoengine.IntField(required=True)
    #user_id    = mongoengine.IntField(required=True)
    texto = mongoengine.StringField(max_length=1024)
    criado_em  = mongoengine.DateTimeField(help_text='criado em')
    modificado_em = mongoengine.DateTimeField(help_text='modificado em', default = datetime.now)
    curtidas   = mongoengine.IntField(required=True, default = 0)

    def save(self, *args, **kwargs):
        if not self.criado_em:
            self.criado_em = datetime.now()
        self.modificado_em = datetime.now()
        return super(Comentario, self).save(*args, **kwargs)

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

    def __str__(self):
        return f"{self.projeto.titulo} - {self.tag.tag}"