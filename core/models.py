from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    #mostra nome no admin
    def __str__(self):
        return self.titulo

    #alterando formato da data e hora
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')    

    #alteração do formato da hora apra editar um agendamento
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')    