from django.contrib import admin
from .models import ContactMessage, HeroSection, Servico, Sobre, ImagemGaleria, ContatoInfo, RedeSocial

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at',)
    
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo',)
    
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao',)
    
    
@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'diferenciais',)
    
    
@admin.register(ImagemGaleria)
class ImagemGaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    
    
@admin.register(ContatoInfo)
class ContatoInfoAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'whatsapp', 'email', 'endereco',)
    
    
@admin.register(RedeSocial)
class RedeSocialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'url',)