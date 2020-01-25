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

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default='', blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    superhost = models.BooleanField(default=False)