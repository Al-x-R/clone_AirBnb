from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ''' Custom User Model '''
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_RUSSIAN = 'ru'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_RUSSIAN, 'Russian'),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_EUR = 'eur'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_EUR, 'EUR'),
    )

    avatar = models.ImageField(upload_to='avatars', blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
