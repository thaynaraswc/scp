from django import forms

from .models import Tipo, Movimentacao, Item

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
        'marca',
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
