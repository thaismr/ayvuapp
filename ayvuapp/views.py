from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect('resource:create')
    else:
        return redirect('login')
