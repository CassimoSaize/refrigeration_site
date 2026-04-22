from django import forms
from .models import ContactMessage
from .models import HeroSection, Servico, Sobre, ImagemGaleria, ContatoInfo, RedeSocial
from .models import OrcamentoSolicitacao

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(84) 99999-9999'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descreva o que precisa...'}),
        }
        

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------



class HeroForm(forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'botao_texto': forms.TextInput(attrs={'class': 'form-control'}),
            'botao_link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'icone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'fas fa-wrench'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SobreForm(forms.ModelForm):
    class Meta:
        model = Sobre
        fields = ['titulo', 'texto', 'diferenciais']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'diferenciais': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Digite um diferencial por linha'}),
        }

class ImagemGaleriaForm(forms.ModelForm):
    class Meta:
        model = ImagemGaleria
        fields = ['titulo', 'imagem', 'ordem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ContatoInfoForm(forms.ModelForm):
    class Meta:
        model = ContatoInfo
        fields = '__all__'
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RedeSocialForm(forms.ModelForm):
    class Meta:
        model = RedeSocial
        fields = '__all__'
        
        

#------------------------------------------------------------------------
#------------------------------------------------------------------------



class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = OrcamentoSolicitacao
        fields = [
            'nome', 'email', 'telefone', 'endereco',
            'tipo_servico', 'tipo_equipamento', 'quantidade',
            'descricao', 'data_preferencial', 'horario_preferencial'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+258 84 000 0000'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro, rua, número...'
            }),
            'tipo_servico': forms.Select(attrs={'class': 'form-select'}),
            'tipo_equipamento': forms.Select(attrs={'class': 'form-select'}),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'value': 1
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Descreva detalhadamente o serviço necessário...'
            }),
            'data_preferencial': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario_preferencial': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_equipamento'].required = False
        self.fields['data_preferencial'].required = False
        self.fields['horario_preferencial'].required = False
        self.fields['endereco'].required = False

class OrcamentoStatusForm(forms.ModelForm):
    class Meta:
        model = OrcamentoSolicitacao
        fields = ['status', 'observacoes', 'valor_orcamento']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Adicione observações internas sobre este orçamento...'
            }),
            'valor_orcamento': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
        }