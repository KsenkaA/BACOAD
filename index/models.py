from .breeds import BREED_CHOICES_DOG, BREED_CHOICES_CAT
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SEX_CHOICE = (
    ("Мальчик", "Мальчик"),
    ("Девочка", "Девочка"),
    )
SIZE_CHOICE = (
    ("Маленький", "Маленький"),
    ("Средний", "Средний"),
    ("Большой", "Большой"),
  )
OWNER_CHOICE = (
    ("Заводчик", "Заводчик"),
    ("Приют", "Приют"),
)
AGE_CHOICE_DOGS = (
    ("Щенок", "Щенок"),
    ("Молодая собака", "Молодая собака"),
    ("Взорлая собака", "Взрослая собака"),
    ("Пожилая собака", "Пожлая собака"),
)
AGE_CATS_CHOICE = (
    ("Котенок", "Котенок"),
    ("Молодая Кошка", "Молодая кошка"),
    ("Взрослая кошка", "Взрослая кошка"),
    ("Пожилая кошка", "Пожилая кошка"),
)
WHO_CHOICE = (
    ('Заводчик', "Заводчик"),
    ("Приют", "Приют"),
    ("Пользователь", "Пользователь")
)


class Cat(models.Model):
    photo = models.ImageField(
        default="..defaultpic.png",
        upload_to='media/'
    )
    age = models.CharField(
        max_length=100,
        choices=AGE_CATS_CHOICE,
    )
    passport = models.BooleanField(
        default=False
    )
    competition = models.BooleanField(
        default=False
    )

    breed = models.CharField(
        max_length=100,
        choices=BREED_CHOICES_CAT,
    )
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICE,
    )
    city = models.CharField(
        max_length=100,
    )
    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICE,
    )
    price = models.IntegerField(
        default=0,
    )
    owner = models.CharField(
        max_length=20,
        choices=OWNER_CHOICE,
    )
    phone = models.CharField(
        max_length=20,
        default='?',
    )


class Dog(models.Model):
    photo = models.ImageField(
        default="..defaultpic.png",
        upload_to='media/'
    )
    age = models.CharField(
        max_length=100,
        choices=AGE_CHOICE_DOGS,
    )
    passport = models.BooleanField(
        default=False
    )
    competition = models.BooleanField(
        default=False
    )
    breed = models.CharField(
        max_length=100,
        choices=BREED_CHOICES_DOG,
    )
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICE,
    )
    city = models.CharField(
        max_length=20,
    )
    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICE,
    )
    price = models.IntegerField(
        default=0,
    )
    owner = models.CharField(
        max_length=20,
        choices=OWNER_CHOICE,
    )
    phone = models.CharField(
        max_length=20,
        default='?',
    )


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=20,
        default='-'
    )
    who = models.CharField(
        max_length=30,
        choices=WHO_CHOICE,
        default='Частное лицо'
    )


@receiver(post_save, sender=User)
def update_user_info(sender, instance, created, **kwargs):
    if created:
        Info.objects.create(user=instance)
    instance.info.save()
