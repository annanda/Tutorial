from django.db import models
import datetime

# Create your models here.

class Enquete(models.Model):
    pergunta = models.CharField('Pergunta', max_length=200)
    data_pub = models.DateTimeField('Data de Publicacao')
    
    def __unicode__(self):
        return self.pergunta

    def foi_publicado_hoje(self):
        return self.data_pub.date() == datetime.date.today()
        
     
    

class Opcao(models.Model):
    enquete = models.ForeignKey(Enquete)
    conteudo = models.CharField(max_length=200)
    votos = models.IntegerField()
    
    def __unicode__(self):
        return self.conteudo
