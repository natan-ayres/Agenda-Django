from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from contact.models import Contact, User


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(owner__username__icontains=search_value) |
            Q(category__name__icontains=search_value)

        )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Busca - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    try:
        single_contact = Contact.objects.get(pk=contact_id, show=True)
    except Contact.DoesNotExist:
        messages.error(request, 'Contato não existente')
        return redirect('contact:index')
        
    site_title = f'{single_contact.first_name}  {single_contact.last_name} -'

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def contactuser(request):
    user = request.user
    site_title = f'{user.username} - '

    context = {
        'contact': user,
        'site_title': site_title
    }

    return render(
        request,
        'contact/user.html',
        context
    )

    