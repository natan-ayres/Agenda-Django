from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact, Category
from django import forms
from django.core.exceptions import ValidationError

def letra_espaco(s):
    return all(caracter.isalpha() or caracter.isspace() for caracter in s)

class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a',
                'placeholder': 'Digite seu nome',
            }
        ),
        label='Nome',
        help_text='Texto para ajudar seu usuário',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a',
                'placeholder': 'Digite seu sobrenome',
            }
        ),
        label='Sobrenome',
        help_text='Texto para ajudar seu usuário',
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a',
                'placeholder': 'Digite seu número',
            }
        ),
        label='Telefone',
        help_text='Texto para ajudar seu usuário',
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a',
                'placeholder': 'Digite seu email',
            }
        ),
        label='E-mail',
        help_text='Texto para ajudar seu usuário',
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'classe-a',
                'placeholder': 'Digite sua descrição',
            }
        ),
        label='Descrição',
        help_text='Texto para ajudar seu usuário',
        required=False
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Categoria',
        help_text='Texto para ajudar seu usuário',
        required=False
    )
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept' : 'pictures/*'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 
            'picture',
        )
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        description = cleaned_data.get('description')
        category = cleaned_data.get('category')
        picture = cleaned_data.get('picture')

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if letra_espaco(first_name) == True:
            ...
        else:
            self.add_error(
                'first_name', ValidationError('Seu nome só pode conter letras.', code='invalid')
            )
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if letra_espaco(last_name) == True:
            ...
        else:
            self.add_error(
                'last_name', ValidationError('Seu sobrenome só pode conter letras.', code='invalid')
            )
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone.isalpha():
            self.add_error(
                'phone', ValidationError('Seu número de celular só pode conter números.', code='invalid')
            )
        else:
            ...
        return phone
