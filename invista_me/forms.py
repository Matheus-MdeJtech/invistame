from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__' # Buscando todas as colunas, caso so alggumas ['nome','valor']