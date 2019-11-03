from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=18)

    def __str__(self):
        return self.nome


class NotaFiscal(models.Model):
    serie = models.CharField(max_length=100, primary_key=True)
    numero = models.IntegerField()
    nome_descricao = models.CharField(max_length=200)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    cubagem = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='notafiscal')

    def __str__(self):
        return self.serie