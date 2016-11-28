from django import forms
from django.contrib.auth.models import User

from .models import Registro, Tipo, Movimentacao, Item, Tarefas

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['user',
        'nome',
        'cpf',
        'dataN',
        'cidade',
        'estado',
        'bairro',
        'telefone',
        'whatsapp',
        'endereco',
        'cep',
        'complemento',
        'lotado',
        'cargo',
        'setor',
        'email',
    ]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['tipo',
        'patrimonio',
        'origem',
    ]

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome',
        'codigo',
        'descricao',
    ]


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['item',
        'modelo',
        'marca',
        'tombo',
        'situacao',
        'servidor',
        'proprietario',
        'local',
    ]

class TarefasForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['tarefa',
    ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split('@')
    #     domain, extension = provider.split('.')
    #     #if not domain == "USC":
    #     #    raise forms.ValidationError("Please make sure you use your USC email")
    #     if not extension == "edu":
    #         raise forms.ValidationError("Please use a valid .EDU email adress")
    #     return email
    #
    # def clean_full_name(self):
    #     full_name = self.cleaned_data.get('full_name')
    #     return full_name
