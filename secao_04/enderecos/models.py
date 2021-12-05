from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    bairro = models.CharField(max_length=255, blank=False, null=False)
    cidade = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(blank=True, null=True)
    cep = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.cidade


# def __str__(self):
#     return '%s, %s, %s, %i, %s' % (self.logradouro, self.bairro, self.cidade, self.numero, self.cep)
