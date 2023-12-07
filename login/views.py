from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('inicio')

    else:
        form = CustomUserCreationForm()

    return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print (user)

        if user is not None:
            login(request, user)
            
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciales inválidas.')

    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('inicio')
