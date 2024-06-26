from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada!')
            return redirect('contact:login')


    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def loginview(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request,'Logado com sucesso! ')
            return redirect('contact:usercontact')
        messages.error(request, 'Login invalido')
    
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logoutview(request):
    auth.logout(request)
    return redirect('contact:login')

def updateview(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)   
         
        if form.is_valid():
            form.save()
            form = AuthenticationForm(request, data=request.POST)
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Atualizado com sucesso! ')
            return redirect('contact:usercontact')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def deleteview(request):
    user = request.user
    user.delete()
    messages.success(request, 'Usuário Deletado')
    return redirect('contact:login')