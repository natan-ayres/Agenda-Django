from django.urls import path


from contact.views import contact, search, index
from contact.views_form import create, update, delete

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', contact, name='contact'),
    path('contact/create/', create, name='create'),
    path('contact/<int:contact_id>/update/', update, name='update'),
    path('contact/<int:contact_id>/delete/', delete, name='delete'),
]