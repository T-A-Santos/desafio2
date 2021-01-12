from django.db import models


class ConsultaPessoa(models.Model):
    CPF = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    lista_dividas = models.CharField(max_length=255)

    def __str__(self):
        return str(self.CPF) + ' - ' + self.nome + ' - ' + self.endereco + ' - ' + self.lista_dividas

    
class ScoreCredito(models.Model):
    CPF = models.ForeignKey(ConsultaPessoa, on_delete=models.CASCADE)
    idade = models.SmallIntegerField()
    lista_bens = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    fonte_renda = models.CharField(max_length=255)

    def __str__(self):
        return str(self.CPF) + ' - ' + self.idade


class RastreaEventos(models.Model):
    CPF = models.ForeignKey(ConsultaPessoa, on_delete=models.CASCADE) 
    ultima_consulta_cpf = models.DateTimeField(auto_now_add=True)
    movimentacao_financeira = models.FloatField()
    dados_relacionados = models.CharField(max_length=255)

    def __str__(self):
        return str(self.CPF) +' - ' + self.ultima_consulta_cpf