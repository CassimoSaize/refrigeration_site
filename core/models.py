from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # NOVO CAMPO

    def __str__(self):
        return f"{self.name} - {self.created_at}"
    
    
#-------------------------------------------------------------

class HeroSection(models.Model):
    titulo = models.CharField('Título', max_length=200, default='Especialista em Ar-Condicionado e Refrigeração em Maputo')
    subtitulo = models.TextField('Subtítulo', default='Instalação, manutenção, reparação e recarga de gás...')
    botao_texto = models.CharField('Texto do botão', max_length=50, default='Solicitar Orçamento')
    botao_link = models.CharField('Link do botão', max_length=200, default='#contato')

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'

    def __str__(self):
        return "Hero da página"

class Servico(models.Model):
    icone = models.CharField('Classe do ícone (FontAwesome)', max_length=50, default='fas fa-wrench')
    titulo = models.CharField('Título do serviço', max_length=100)
    descricao = models.TextField('Descrição')
    ordem = models.IntegerField('Ordem de exibição', default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.titulo

class Sobre(models.Model):
    titulo = models.CharField('Título da seção', max_length=100, default='Sobre mim')
    texto = models.TextField('Texto principal')
    icone_diferencial = models.CharField('Ícone dos diferenciais', max_length=50, default='fas fa-check-circle')
    # Diferenciais serão salvos como uma lista separada por linhas
    diferenciais = models.TextField('Lista de diferenciais (um por linha)', help_text='Exemplo:\nDiagnóstico rápido\nPeças originais')

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return self.titulo

    def get_diferenciais_list(self):
        return [item.strip() for item in self.diferenciais.split('\n') if item.strip()]

class ImagemGaleria(models.Model):
    titulo = models.CharField('Título/Alt', max_length=200, blank=True)
    imagem = models.ImageField('Imagem', upload_to='galeria/')
    ordem = models.IntegerField('Ordem', default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Imagem da Galeria'
        verbose_name_plural = 'Imagens da Galeria'

    def thumbnail(self):
        return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />', self.imagem.url)
    thumbnail.short_description = 'Pré-visualização'

    def __str__(self):
        return self.titulo or f"Imagem {self.id}"

class ContatoInfo(models.Model):
    telefone = models.CharField('Telefone', max_length=20, default='+258 84 000 0000')
    whatsapp = models.CharField('WhatsApp (número com código)', max_length=20, default='258840000000')
    email = models.EmailField('E-mail', default='cassimosaize@refrigeracao.com')
    endereco = models.CharField('Endereço', max_length=200, default='Maputo - Moçambique')

    class Meta:
        verbose_name = 'Informação de Contato'
        verbose_name_plural = 'Informação de Contato'

    def __str__(self):
        return "Contatos principais"

class RedeSocial(models.Model):
    nome = models.CharField('Rede social', max_length=50)  # facebook, instagram, etc
    url = models.URLField('Link')
    icone = models.CharField('Classe do ícone', max_length=50, default='fab fa-facebook')
    ordem = models.IntegerField('Ordem', default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return self.nome
    
    
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

class OrcamentoSolicitacao(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('viewed', 'Visualizado'),
        ('contacted', 'Em contato'),
        ('budget_sent', 'Orçamento enviado'),
        ('approved', 'Aprovado'),
        ('rejected', 'Recusado'),
        ('completed', 'Concluído'),
    )

    # Dados pessoais
    nome = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone/WhatsApp', max_length=20)
    endereco = models.CharField('Endereço', max_length=200, blank=True)

    # Dados do serviço
    tipo_servico = models.CharField('Tipo de serviço', max_length=50, choices=[
        ('instalacao', 'Instalação de Ar-Condicionado'),
        ('manutencao', 'Manutenção Preventiva'),
        ('reparacao', 'Reparação/Conserto'),
        ('limpeza', 'Limpeza de equipamentos'),
        ('recarga', 'Recarga de Gás'),
        ('outros', 'Outros serviços'),
    ])

    tipo_equipamento = models.CharField('Tipo de equipamento', max_length=50, choices=[
        ('split', 'Ar-Condicionado Split'),
        ('cassete', 'Ar-Condicionado Cassete'),
        ('piso_teto', 'Piso-Teto'),
        ('janela', 'Ar-Condicionado de Janela'),
        ('camara_fria', 'Câmara Fria'),
        ('freezer', 'Freezer/Refrigerador'),
        ('outros', 'Outros'),
    ], blank=True)

    quantidade = models.PositiveIntegerField('Quantidade de equipamentos', default=1)
    descricao = models.TextField('Descrição detalhada do serviço')
    data_preferencial = models.DateField('Data preferencial para atendimento', null=True, blank=True)
    horario_preferencial = models.CharField('Horário preferencial', max_length=50, blank=True, choices=[
        ('manha', 'Manhã (8h-12h)'),
        ('tarde', 'Tarde (13h-17h)'),
        ('noite', 'Noite (18h-21h)'),
        ('qualquer', 'Qualquer horário'),
    ])

    # Metadados
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pending')
    observacoes = models.TextField('Observações internas', blank=True, help_text='Anotações da equipe sobre este orçamento')
    valor_orcamento = models.DecimalField('Valor do orçamento', max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField('Data da solicitação', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    viewed_at = models.DateTimeField('Data de visualização', null=True, blank=True)

    class Meta:
        verbose_name = 'Solicitação de Orçamento'
        verbose_name_plural = 'Solicitações de Orçamento'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_servico_display()} - {self.created_at.strftime('%d/%m/%Y')}"

    def mark_as_viewed(self):
        if not self.viewed_at:
            self.viewed_at = timezone.now()
            if self.status == 'pending':
                self.status = 'viewed'
            self.save()