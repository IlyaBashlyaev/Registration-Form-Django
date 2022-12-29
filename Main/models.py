from django.db import models

class Account(models.Model):
    username = models.CharField('Username', max_length = 100)
    email = models.CharField('Email', max_length = 100)
    password = models.CharField('Password', max_length = 100)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'