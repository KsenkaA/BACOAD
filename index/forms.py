from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .breeds import BREED_CHOICES_DOG, BREED_CHOICES_CAT
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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    who = forms.ChoiceField(choices=WHO_CHOICE)

    class Meta:
        model = User
        fields = ('username', 'who', 'first_name', 'last_name', 'email', 'password1', 'password2', )

