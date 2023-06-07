from django.db import models
from datetime import datetime

# Create your models here.
class Investimento(models.Model):
    investimento = models.TextField(max_length=225)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)

# Sempre que for adicionar ou remover coluna ou tabela rodar o codigo
# > python manage.py makemigrations

# E apos isso rodar
# > python manage.py migrate

