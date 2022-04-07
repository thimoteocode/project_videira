from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativo']
        # fields = ['__all__']
