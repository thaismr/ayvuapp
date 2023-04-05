from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect('resource:list')
    else:
        return redirect('login')
