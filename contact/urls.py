from django.urls import path


from contact.views import contact, search, index, contactuser
from contact.views_form import create, update, delete
from contact.user_form import register, loginview, logoutview, updateview

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),

    path('contact/<int:contact_id>/', contact, name='contact'),
    path('contact/create/', create, name='create'),
    path('contact/<int:contact_id>/update/', update, name='update'),
    path('contact/<int:contact_id>/delete/', delete, name='delete'),

    path('user/create/', register, name='register'),
    path('user/login/', loginview, name='login'),
    path('user/logout/', logoutview, name='logout'),
    path('user/update/', updateview, name='userupdate'),
    path('user/contact/', contactuser, name='usercontact'),
]