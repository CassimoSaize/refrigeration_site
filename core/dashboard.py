from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import ContactMessage
from .decorators import admin_required

def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard_home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Credenciais inválidas ou acesso não autorizado.')
    return render(request, 'dashboard/login.html')

def dashboard_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('dashboard_login')

@admin_required
def dashboard_home(request):
    # Estatísticas
    total_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    
    # Mensagens dos últimos 30 dias
    thirty_days_ago = timezone.now() - timedelta(days=30)
    recent_messages = ContactMessage.objects.filter(created_at__gte=thirty_days_ago).count()
    
    # Mensagens por dia (últimos 7 dias)
    last_7_days = []
    for i in range(6, -1, -1):
        date = timezone.now().date() - timedelta(days=i)
        count = ContactMessage.objects.filter(created_at__date=date).count()
        last_7_days.append({
            'date': date.strftime('%d/%m'),
            'count': count
        })
    
    context = {
        'total_messages': total_messages,
        'unread_messages': unread_messages,
        'recent_messages': recent_messages,
        'last_7_days': last_7_days,
    }
    return render(request, 'dashboard/home.html', context)

@admin_required
def dashboard_messages(request):
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    
    # Filtros
    status_filter = request.GET.get('status')
    if status_filter == 'read':
        messages_list = messages_list.filter(is_read=True)
    elif status_filter == 'unread':
        messages_list = messages_list.filter(is_read=False)
    
    search = request.GET.get('search')
    if search:
        messages_list = messages_list.filter(
            Q(name__icontains=search) | 
            Q(phone__icontains=search) |
            Q(message__icontains=search)
        )
    
    context = {
        'messages': messages_list,
        'total_count': messages_list.count(),
        'current_filter': status_filter,
        'search_term': search,
    }
    return render(request, 'dashboard/messages.html', context)

@admin_required
def dashboard_message_detail(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'dashboard/message_detail.html', {'message': message})

@admin_required
def dashboard_message_delete(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.delete()
    messages.success(request, 'Mensagem excluída com sucesso.')
    return redirect('dashboard_messages')