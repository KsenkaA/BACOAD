from .models import Cat, Dog
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from .breeds import a, b
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/search_form/')
    return render_to_response('new_login.html')


def signup(request):
    if request.method == 'POST':
        usernames = []
        for user in User.objects.all():
            usernames.append(user.username)
        if request.POST['username'] not in usernames:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],
                                            email=request.POST['email'], first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'])
            user.refresh_from_db()
            user.info.who = request.POST['who']
            user.info.phone_number = request.POST['phone_number']
            user.save()
            raw_password = request.POST['password1']
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'testtest.html', {})
        else:
            message = 'К сожалению, это ник уже занят, попробуйте снова'
            return render(request, 'new_registration.html', {'message': message})
    else:
        return render(request, 'new_registration.html', {'message': ''})


# kG45yrv8 Kg45yrv8 kg45Yrv8 kg45yrV8 204/206
def search_form(request):
    return render(request, 'new_search_form.html', {
        'WHO_CHOICE': WHO_CHOICE,
        'AGE_CATS_CHOICE': AGE_CATS_CHOICE,
        'AGE_CHOICE_DOGS': AGE_CHOICE_DOGS,
        'OWNER_CHOICE': OWNER_CHOICE,
        'SIZE_CHOICE': SIZE_CHOICE,
        'BREED_CHOICES_CAT': b,
        'BREED_CHOICES_DOG': a,
        'cities': ['Белгород', 'Волгоград', 'Вологда', 'Йошкар-Ола', 'Казань', 'Калуга', 'Кемерово', 'Краснодар',
                   'Курск', 'Липецк', 'Москва', 'Санкт-Петербург', 'Смоленск', 'Саранск', 'Ставрополь', 'Тамбов',
                   'Томск', 'Тула', 'Тюмень', 'Ханты-Мансийск']
    })


def search(request):
    search_params = {}
    for i in request.GET.items():
        if 'Выберите' in i[1]:
            search_params[i[0]] = ''
        else:
            search_params[i[0]] = i[1]
    if 'competition' in search_params.keys():
        print('momo')
        search_params['competition'] = True
    else:
        print('ililil')
        search_params['competition'] = ''
    if 'passport' in search_params.keys():
        print('kpkpk')
        search_params['passport'] = True
    else:
        print('lklklk')
        search_params['passport'] = ''
    if search_params['price'] == '':
        search_params['price'] = 1000000
    if search_params['type'] == 'Кошка':
        if search_params['competition'] == '':
            if search_params['passport'] == '':
                print('kikiki')
                context = {
                    'animals': Cat.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'])
                }
            else:
                print('kokoko')
                context = {
                    'animals': Cat.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'],
                                                  passport=search_params['passport'])
                }
        else:
            if search_params['passport'] == '':
                print('lololo')
                context = {
                    'animals': Cat.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  competition=search_params['competition'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'])
                }
            else:
                print('kakaka')
                context = {
                    'animals': Cat.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  competition=search_params['competition'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'],
                                                  passport=search_params['passport'])
                }
        return render(request, 'new_search.html', context)
    elif search_params['type'] == 'Собака':
        if search_params['competition'] == '':
            if search_params['passport'] == '':
                print('kikiki')
                context = {
                    'animals': Dog.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'])
                }
            else:
                print('kokoko')
                context = {
                    'animals': Dog.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'],
                                                  passport=search_params['passport'])
                }
            return render(request, 'new_search.html', context)
        else:
            if search_params['passport'] == '':
                print('lololo')
                context = {
                    'animals': Dog.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  competition=search_params['competition'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'])
                }
            else:
                print('kakaka')
                context = {
                    'animals': Dog.objects.filter(age__contains=request.GET['age'],
                                                  breed__contains=request.GET['breed'],
                                                  city__contains=request.GET['city'],
                                                  price__lte=int(search_params['price']),
                                                  sex__contains=request.GET['sex'],
                                                  competition=search_params['competition'],
                                                  size__contains=request.GET['size'],
                                                  owner__contains=request.GET['owner'],
                                                  passport=search_params['passport'])
                }
            return render(request, 'new_search.html', context)


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


@login_required(login_url='/index/login/')
def adding(request):
    if request.method == "POST":
        if 'competition' in request.POST.keys():
            competition_ = True
        else:
            competition_ = False
        if 'passport' in request.POST.keys():
            passport_ = True
        else:
            passport_ = False
        print(request.FILES.keys())
        if request.POST['type'] == 'Кошка':
            myfile = request.FILES['photo']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)

            cat = Cat.objects.create(photo=request.FILES['photo'], age=request.POST['age'], breed=request.POST['breed'],
                                     city=request.POST['city'],
                                     price=int(request.POST['price']), phone=request.user.info.phone_number, sex=request.POST['sex'],
                                     competition=competition_, size=request.POST['size'],
                                     owner=request.user.info.who, passport=passport_)
            cat.save()
        elif request.POST['type'] == 'Собака':
            myfile = request.FILES['photo']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            dog = Dog.objects.create(photo=request.FILES['photo'], age=request.POST['age'], breed=request.POST['breed'],
                                     city=request.POST['city'],
                                     price=int(request.POST['price']), phone=request.user.info.phone_number, sex=request.POST['sex'],
                                     competition=competition_, size=request.POST['size'],
                                     owner=request.user.info.who, passport=passport_)
            dog.save()
        return render(request, 'testtest.html', {})
    else:
        if request.user.info.who == 'Заводчик' or request.user.info.who == 'Приют':
            context = {
                'WHO_CHOICE': WHO_CHOICE,
                'AGE_CATS_CHOICE': AGE_CATS_CHOICE,
                'AGE_CHOICE_DOGS': AGE_CHOICE_DOGS,
                'OWNER_CHOICE': OWNER_CHOICE,
                'SIZE_CHOICE': SIZE_CHOICE,
                'BREED_CHOICES_CAT': b,
                'BREED_CHOICES_DOG': a,
                'cities': ['Белгород', 'Волгоград', 'Вологда', 'Йошкар-Ола', 'Казань', 'Калуга', 'Кемерово',
                           'Краснодар', 'Курск', 'Липецк', 'Москва', 'Санкт-Петербург', 'Смоленск', 'Саранск',
                           'Ставрополь', 'Тамбов', 'Томск', 'Тула', 'Тюмень', 'Ханты-Мансийск']
            }

            return render(request, 'new_adding.html', context)
        else:
            return render(request, 'testtest.html', {'user': request.user})
