from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Faça login para acessar o dashboard.')
            return redirect('dashboard_login')
        if not request.user.is_staff:
            messages.error(request, 'Acesso restrito a administradores.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper