from django import forms

from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nome',
        'cpf',
        'dataN',
        'cidade',
        'estado',
        'bairro',
        'telefone',
        'whatsapp',
        'adress',
        'cep',
        'complemento',
        'lotado',
        'cargo',
        'setor',
        'email',
    ]

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
