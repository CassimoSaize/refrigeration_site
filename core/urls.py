from django.urls import path
from . import views
from . import dashboard
from .views import orcamento_detail, orcamento_export_pdf, orcamento_export_excel

urlpatterns = [
    path('', views.home, name='home'),
    
    # Dashboard routes
    path('admin-dashboard/', dashboard.dashboard_home, name='dashboard_home'),
    path('admin-dashboard/login/', dashboard.dashboard_login, name='dashboard_login'),
    path('admin-dashboard/logout/', dashboard.dashboard_logout, name='dashboard_logout'),
    path('admin-dashboard/mensagens/', dashboard.dashboard_messages, name='dashboard_messages'),
    path('admin-dashboard/mensagem/<int:message_id>/', dashboard.dashboard_message_detail, name='dashboard_message_detail'),
    path('admin-dashboard/mensagem/<int:message_id>/deletar/', dashboard.dashboard_message_delete, name='dashboard_message_delete'),
    
    
    path('hero/', views.hero_edit, name='hero_edit'),
    path('servicos/', views.servico_list, name='servico_list'),
    path('servicos/criar/', views.servico_create, name='servico_create'),
    path('servicos/editar/<int:pk>/', views.servico_edit, name='servico_edit'),
    path('servicos/deletar/<int:pk>/', views.servico_delete, name='servico_delete'),
    path('galeria/', views.galeria_list, name='galeria_list'),
    path('galeria/criar/', views.galeria_create, name='galeria_create'),
    path('galeria/editar/<int:pk>/', views.galeria_edit, name='galeria_edit'),
    path('galeria/deletar/<int:pk>/', views.galeria_delete, name='galeria_delete'),
    path('sobre/', views.sobre_edit, name='sobre_edit'),
    path('contato/', views.contato_edit, name='contato_edit'),
    path('contato/criar/', views.contato_create, name='contato_create'),
    
    
    path('solicitar-orcamento/', views.solicitar_orcamento, name='solicitar_orcamento'),
    path('orcamentos/', views.orcamento_list, name='orcamento_list'),
    path('orcamentos/<int:pk>/', views.orcamento_detail, name='orcamento_detail'),
    path('orcamentos/<int:pk>/deletar/', views.orcamento_delete, name='orcamento_delete'),
    path('orcamento/<int:pk>/pdf/', orcamento_export_pdf, name='orcamento_export_pdf'),
    path('orcamento/<int:pk>/excel/', orcamento_export_excel, name='orcamento_export_excel'),
]