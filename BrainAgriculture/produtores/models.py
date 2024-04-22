from django.db import models


class Produtor(models.Model):
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    nome_fazenda = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    area_total_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    area_agricultavel_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    area_vegetacao_hectares = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Cultura(models.Model):
    nome = models.CharField(max_length=100)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name="culturas")

    def __str__(self):
        return self.nome_cultura
