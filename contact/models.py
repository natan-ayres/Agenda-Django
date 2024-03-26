from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank= True)
    email = models.EmailField(max_length=254, blank= True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to= 'pictures/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        blank=True, null=True,
        )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        blank=True, null=True,
        )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
@receiver(pre_save, sender=Contact)
def set_contact_owner(sender, instance, **kwargs):
        if not instance.owner_id:
            instance.owner = instance._request_user