from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact, Category, User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

def letra_espaco(s):
    return all(caracter.isalpha() or caracter.isspace() for caracter in s)



class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu nome',
            }
        ),
        label='Nome',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu sobrenome',
            }
        ),
        label='Sobrenome',
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu número',
            }
        ),
        label='Telefone',
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu email',
            }
        ),
        label='E-mail',
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Digite sua descrição',
            }
        ),
        label='Descrição',
        required=False
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Categoria',
        required=False
    )
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept' : 'pictures/*'
            }
        ),
        label='Foto',
        required=False
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

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu nome',
            }
        ),
        label= 'Nome',
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu sobrenome',
            }
        ),
        label= 'Sobrenome',
        required=True,
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu email',
            }
        ),
        label= 'E-mail',
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu usuário',
            }
        ),
        label = 'Usuário',
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha',
            }
        ),
        label = 'Senha',
        required=True,
        help_text= 'Acima de 8 dígitos'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha novamente',
            }
        ),
        label = 'Confirme a senha' ,
        required=True,
    )


    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email
    