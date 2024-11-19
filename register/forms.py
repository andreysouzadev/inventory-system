from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.Form):
    # nome_completo = forms.CharField(required=True, error_messages={'required': 'O campo Nome Completo é obrigatório.'})
    nome_completo = forms.CharField(
    label="Nome Completo",
    required=True,
    max_length=100,
    widget=forms.TextInput(attrs={
        'placeholder': 'Nome Completo',
        'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
    })
)
    username = forms.EmailField(required=True, error_messages={'required': 'O campo E-mail é obrigatório.'})
    telefone = forms.CharField(
        required=True, 
        error_messages={'required': 'O campo Telefone é obrigatório.'},
    )
    funcao = forms.ChoiceField(
        choices=[
            ('', 'Selecione sua função'),
            ('analista-noc', 'Analista NOC'),
            ('analista-soc', 'Analista SOC'),
            ('especialistas', 'Especialistas'),
        ],
        required=True,
        error_messages={'required': 'O campo Função é obrigatório.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        error_messages={'required': 'O campo Senha é obrigatório.'}
    )
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        error_messages={'required': 'A confirmação da senha é obrigatória.'}
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if password and confirmar_senha and password != confirmar_senha:
            self.add_error('confirmar_senha', 'As senhas não coincidem.')

    def clean_nome_completo(self):
        nome = self.cleaned_data['nome_completo']
        if len(nome) < 3:
            raise forms.ValidationError("O nome completo deve ter pelo menos 3 caracteres.")
        return nome





