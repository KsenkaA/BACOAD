# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20180121_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.CharField(choices=[('Котенок', 'Котенок'), ('Молодая Кошка', 'Молодая кошка'), ('Взрослая кошка', 'Взрослая кошка'), ('Пожилая кошка', 'Пожилая кошка')], max_length=100),
        ),
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(choices=[('Без породы', 'Без породы'), ('Абиссинская', 'Абиссинская'), ('Австралийский мист', 'Австралийский мист'), ('Азиатская (Табби)', 'Азиатская (Табби)'), ('Акринская', 'Акринская'), ('Американская жесткошёрстная', 'Американская жесткошёрстная'), ('Американская короткошёрстная', 'Американская короткошёрстная'), ('Американский бобтейл длинношёрстный', 'Американский бобтейл длинношёрстный'), ('Американский бобтейл короткошёрстный', 'Американский бобтейл короткошёрстный'), ('Американский кёрл длинношёрстный', 'Американский кёрл длинношёрстный'), ('Американский кёрл короткошёрстный', 'Американский кёрл короткошёрстный'), ('Анатолийская', 'Анатолийская'), ('Аравийский мау', 'Аравийский мау'), ('Балинезийская (Балийская)', 'Балинезийская (Балийская)'), ('Бенгальская', 'Бенгальская'), ('Бомбейская', 'Бомбейская'), ('Бразильская короткошёрстная', 'Бразильская короткошёрстная'), ('Британская длинношёрстная', 'Британская длинношёрстная'), ('Британская короткошёрстная', 'Британская короткошёрстная'), ('Бурма (Бурманская)', 'Бурма (Бурманская)'), ('Бурмилла длинношёрстный', 'Бурмилла длинношёрстный'), ('Бурмилла короткошёрстный', 'Бурмилла короткошёрстный'), ('Гавана', 'Гавана'), ('Гималайская кошка', 'Гималайская кошка'), ('Девон рекс', 'Девон рекс'), ('Домашняя', 'Домашняя'), ('Донской сфинкс', 'Донской сфинкс'), ('Египетская мау', 'Египетская мау'), ('Калифорнийская сияющая', 'Калифорнийская сияющая'), ('Канаани', 'Канаани'), ('Карельский бобтейл длинношёрстный', 'Карельский бобтейл длинношёрстный'), ('Карельский бобтейл короткошёрстный', 'Карельский бобтейл короткошёрстный'), ('Кельтская (Европейская короткошёрстная)', 'Кельтская (Европейская короткошёрстная)'), ('Кимрик', 'Кимрик'), ('Колорпойнт', 'Колорпойнт'), ('Корат', 'Корат'), ('Корниш рекс', 'Корниш рекс'), ('Курильский бобтейл длинношёрстный', 'Курильский бобтейл длинношёрстный'), ('Курильский бобтейл короткошёрстный', 'Курильский бобтейл короткошёрстный'), ('Лаперм длинношёрстный', 'Лаперм длинношёрстный'), ('Лаперм короткошёрстный', 'Лаперм короткошёрстный'), ('Манчкин длинношёрстная', 'Манчкин длинношёрстная'), ('Манчкин короткошёрстная', 'Манчкин короткошёрстная'), ('Мейн-кун', 'Мейн-кун'), ('Меконгский бобтейл', 'Меконгский бобтейл'), ('Минскин', 'Минскин'), ('Мэнкс (Мэнская кошка)', 'Мэнкс (Мэнская кошка)'), ('Наполеон', 'Наполеон'), ('Невская маскарадная', 'Невская маскарадная'), ('Немецкий рекс', 'Немецкий рекс'), ('Нибелунг', 'Нибелунг'), ('Норвежская лесная', 'Норвежская лесная'), ('Орегон-рекс', 'Орегон-рекс'), ('Ориентальная длинношёрстная', 'Ориентальная длинношёрстная'), ('Ориентальная короткошёрстная', 'Ориентальная короткошёрстная'), ('Охос азулес', 'Охос азулес'), ('Охос азулес длинношёрстный', 'Охос азулес длинношёрстный'), ('Оцикет', 'Оцикет'), ('Персидская (Колорпойнт)', 'Персидская (Колорпойнт)'), ('Петерболд', 'Петерболд'), ('Пиксибоб длинношёрстный', 'Пиксибоб длинношёрстный'), ('Пиксибоб короткошёрстный', 'Пиксибоб короткошёрстный'), ('Рагамаффин', 'Рагамаффин'), ('Русская голубая', 'Русская голубая'), ('Рэгдолл', 'Рэгдолл'), ('Саванна', 'Саванна'), ('Священная бирманская', 'Священная бирманская'), ('Сейшельская длинношёрстная', 'Сейшельская длинношёрстная'), ('Сейшельская короткошёрстная', 'Сейшельская короткошёрстная'), ('Селкирк рекс длинношёрстный', 'Селкирк рекс длинношёрстный'), ('Селкирк рекс короткошёрстный', 'Селкирк рекс короткошёрстный'), ('Серенгети', 'Серенгети'), ('Сиамская', 'Сиамская'), ('Сибирская', 'Сибирская'), ('Сингапурская', 'Сингапурская'), ('Скоттиш страйт', 'Скоттиш страйт'), ('Скоттиш фолд', 'Скоттиш фолд'), ('Сноу-Шу', 'Сноу-Шу'), ('Сококе', 'Сококе'), ('Сомали', 'Сомали'), ('Сфинкс (Канадский)', 'Сфинкс (Канадский)'), ('Тайская', 'Тайская'), ('Тойгер', 'Тойгер'), ('Тонкинская', 'Тонкинская'), ('Турецкая ангора', 'Турецкая ангора'), ('Турецкий ван', 'Турецкий ван'), ('Украинский левкой', 'Украинский левкой'), ('Уральский рекс длинношёрстный', 'Уральский рекс длинношёрстный'), ('Уральский рекс короткошёрстный', 'Уральский рекс короткошёрстный'), ('Форин Вайт', 'Форин Вайт'), ('Хайленд фолд', 'Хайленд фолд'), ('Цейлонская', 'Цейлонская'), ('Чаузи', 'Чаузи'), ('Шантильи Тиффаны', 'Шантильи Тиффаны'), ('Шартрез', 'Шартрез'), ('Эгейская', 'Эгейская'), ('Экзотическая', 'Экзотическая'), ('Экспериментальная порода', 'Экспериментальная порода'), ('Яванез (Яванская)', 'Яванез (Яванская)'), ('Японский бобтейл длинношёрстный', 'Японский бобтейл длинношёрстный'), ('Японский бобтейл короткошёрстный', 'Японский бобтейл короткошёрстный')], max_length=100),
        ),
        migrations.AlterField(
            model_name='cat',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.CharField(choices=[('Заводчик', 'Заводчик'), ('Приют', 'Приют')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cat',
            name='size',
            field=models.CharField(choices=[('Маленький', 'Маленький'), ('Средний', 'Средний'), ('Большой', 'Большой')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.CharField(choices=[('Щенок', 'Щенок'), ('Молодая собака', 'Молодая собака'), ('Взорлая собака', 'Взрослая собака'), ('Пожилая собака', 'Пожлая собака')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(choices=[('Без породы', 'Без породы'), ('Австралийская короткохвостая пастушья собака', 'Австралийская короткохвостая пастушья собака'), ('Австралийская овчарка', 'Австралийская овчарка'), ('Австралийская пастушья собака', 'Австралийская пастушья собака'), ('Австралийский келпи', 'Австралийский келпи'), ('Австралийский терьер', 'Австралийский терьер'), ('Австралийский шелковистый терьер', 'Австралийский шелковистый терьер'), ('Австрийская гончая', 'Австрийская гончая'), ('Австрийский брудастый бракк', 'Австрийский брудастый бракк'), ('Австрийский пинчер', 'Австрийский пинчер'), ('Азавак', 'Азавак'), ('Азорская пастушья собака', 'Азорская пастушья собака'), ('Аиди', 'Аиди'), ('Акита-ину', 'Акита-ину'), ('Алан', 'Алан'), ('Алано', 'Алано'), ('Алапахский бульдог', 'Алапахский бульдог'), ('Альпийская таксообразная гончая', 'Альпийская таксообразная гончая'), ('Аляскинский кли-кай', 'Аляскинский кли-кай'), ('Аляскинский маламут', 'Аляскинский маламут'), ('Американская акита', 'Американская акита'), ('Американская эскимосская собака', 'Американская эскимосская собака'), ('Американский бандог', 'Американский бандог'), ('Американский бульдог', 'Американский бульдог'), ('Американский водяной спаниель', 'Американский водяной спаниель'), ('Американский голый терьер', 'Американский голый терьер'), ('Американский кокер-спаниель', 'Американский кокер-спаниель'), ('Американский мастиф', 'Американский мастиф'), ('Американский питбультерьер', 'Американский питбультерьер'), ('Американский стаффордширский терьер', 'Американский стаффордширский терьер'), ('Американский фоксхаунд', 'Американский фоксхаунд'), ('Анатолийская овчарка', 'Анатолийская овчарка'), ('Английская енотовая гончая', 'Английская енотовая гончая'), ('Английская овчарка', 'Английская овчарка'), ('Английский бульдог', 'Английский бульдог'), ('Английский водяной спаниель', 'Английский водяной спаниель'), ('Английский кокер-спаниель', 'Английский кокер-спаниель'), ('Английский мастиф', 'Английский мастиф'), ('Английский пойнтер', 'Английский пойнтер'), ('Английский сеттер', 'Английский сеттер'), ('Английский спрингер-спаниель', 'Английский спрингер-спаниель'), ('Английский той-терьер', 'Английский той-терьер'), ('Английский фоксхаунд', 'Английский фоксхаунд'), ('Англо-французская малая гончая', 'Англо-французская малая гончая'), ('Аппенцеллер зенненхунд', 'Аппенцеллер зенненхунд'), ('Аргентинский дог', 'Аргентинский дог'), ('Арденнский бувье', 'Арденнский бувье'), ('Артуазская гончая', 'Артуазская гончая'), ('Афганская борзая', 'Афганская борзая'), ('Аффенпинчер', 'Аффенпинчер'), ('Баварская горная гончая', 'Баварская горная гончая'), ('Бакхмуль', 'Бакхмуль'), ('Барбет (собака)', 'Барбет (собака)'), ('Басенджи', 'Басенджи'), ('Баскская овчарка', 'Баскская овчарка'), ('Бассет-хаунд', 'Бассет-хаунд'), ('Бедлингтон-терьер', 'Бедлингтон-терьер'), ('Белая швейцарская овчарка', 'Белая швейцарская овчарка'), ('Бельгийская овчарка', 'Бельгийская овчарка'), ('Бельгийский гриффон', 'Бельгийский гриффон'), ('Бергамская овчарка', 'Бергамская овчарка'), ('Бернская гончая', 'Бернская гончая'), ('Бернский зенненхунд', 'Бернский зенненхунд'), ('Бивер-йоркширский терьер', 'Бивер-йоркширский терьер'), ('Бигль', 'Бигль'), ('Бишон фризе', 'Бишон фризе'), ('Бладхаунд', 'Бладхаунд'), ('Блю-лейси', 'Блю-лейси'), ('Бобтейл', 'Бобтейл'), ('Болгарский барак', 'Болгарский барак'), ('Болоньез', 'Болоньез'), ('Большой вандейский бассет-гриффон', 'Большой вандейский бассет-гриффон'), ('Большой вандейский гриффон', 'Большой вандейский гриффон'), ('Большой швейцарский зенненхунд', 'Большой швейцарский зенненхунд'), ('Бордер-колли', 'Бордер-колли'), ('Бордер-терьер', 'Бордер-терьер'), ('Бордоский дог', 'Бордоский дог'), ('Бородатый колли', 'Бородатый колли'), ('Босерон', 'Босерон'), ('Бостон-терьер', 'Бостон-терьер'), ('Бразильский терьер', 'Бразильский терьер'), ('Бразильский фила', 'Бразильский фила'), ('Бретонский эпаньоль', 'Бретонский эпаньоль'), ('Бриар (порода собак)', 'Бриар (порода собак)'), ('Брохольмер', 'Брохольмер'), ('Брюссельский гриффон', 'Брюссельский гриффон'), ('Буковинская овчарка', 'Буковинская овчарка'), ('Бульдог кампейро', 'Бульдог кампейро'), ('Бульдог Катахулы', 'Бульдог Катахулы'), ('Бульмастиф', 'Бульмастиф'), ('Бультерьер', 'Бультерьер'), ('Бурбуль', 'Бурбуль'), ('Бурят-монгольский волкодав', 'Бурят-монгольский волкодав'), ('Валенсийский ратер', 'Валенсийский ратер'), ('Вандейский бассет-гриффон', 'Вандейский бассет-гриффон'), ('Веймаранер', 'Веймаранер'), ('Вельш-корги', 'Вельш-корги'), ('Вельш-спрингер-спаниель', 'Вельш-спрингер-спаниель'), ('Вельштерьер', 'Вельштерьер'), ('Венгерская выжла', 'Венгерская выжла'), ('Вертельная собака', 'Вертельная собака'), ('Вест-хайленд-уайт-терьер', 'Вест-хайленд-уайт-терьер'), ('Веттерхун', 'Веттерхун'), ('Волчья собака Сарлоса', 'Волчья собака Сарлоса'), ('Вольпино итальяно', 'Вольпино итальяно'), ('Восточноевропейская овчарка', 'Восточноевропейская овчарка'), ('Восточносибирская лайка', 'Восточносибирская лайка'), ('Гаванский бишон', 'Гаванский бишон'), ('Гамильтонстёваре', 'Гамильтонстёваре'), ('Гампр', 'Гампр'), ('Гладкошёрстный фокстерьер', 'Гладкошёрстный фокстерьер'), ('Глен оф Имаал терьер', 'Глен оф Имаал терьер'), ('Голландская овчарка', 'Голландская овчарка'), ('Голландский смоусхонд', 'Голландский смоусхонд'), ('Голубой гасконский бассет', 'Голубой гасконский бассет'), ('Гончая Шиллера', 'Гончая Шиллера'), ('Грейхаунд', 'Грейхаунд'), ('Гренландская собака', 'Гренландская собака'), ('Греческая овчарка', 'Греческая овчарка'), ('Грюнендаль', 'Грюнендаль'), ('Далматин', 'Далматин'), ('Датско-шведская фермерская собака', 'Датско-шведская фермерская собака'), ('Денди-динмонт-терьер', 'Денди-динмонт-терьер'), ('Джек-рассел-терьер', 'Джек-рассел-терьер'), ('Дзёмон-сиба', 'Дзёмон-сиба'), ('Дирхаунд', 'Дирхаунд'), ('Длинношерстная акита-ину', 'Длинношерстная акита-ину'), ('Длинношёрстный колли', 'Длинношёрстный колли'), ('Доберман', 'Доберман'), ('Дратхаар', 'Дратхаар'), ('Древер', 'Древер'), ('Евразиер', 'Евразиер'), ('Жесткошёрстный фокстерьер', 'Жесткошёрстный фокстерьер'), ('Западносибирская лайка', 'Западносибирская лайка'), ('Золотистый ретривер', 'Золотистый ретривер'), ('Ирландский водяной спаниель', 'Ирландский водяной спаниель'), ('Ирландский волкодав', 'Ирландский волкодав'), ('Ирландский красный сеттер', 'Ирландский красный сеттер'), ('Ирландский мягкошёрстный пшеничный терьер', 'Ирландский мягкошёрстный пшеничный терьер'), ('Ирландский терьер', 'Ирландский терьер'), ('Исландская собака', 'Исландская собака'), ('Испанская водяная собака', 'Испанская водяная собака'), ('Испанский гальго', 'Испанский гальго'), ('Испанский мастиф', 'Испанский мастиф'), ('Итальянский бракк', 'Итальянский бракк'), ('Итальянский спиноне', 'Итальянский спиноне'), ('Йоркширский терьер', 'Йоркширский терьер'), ('Ка-де-бо', 'Ка-де-бо'), ('Кавалер-кинг-чарльз-спаниель', 'Кавалер-кинг-чарльз-спаниель'), ('Кавказская овчарка', 'Кавказская овчарка'), ('Каи (порода собак)', 'Каи (порода собак)'), ('Канарский дог', 'Канарский дог'), ('Кане-корсо', 'Кане-корсо'), ('Као де кастро-лаборейро', 'Као де кастро-лаборейро'), ('Каракачанская собака', 'Каракачанская собака'), ('Карело-финская лайка', 'Карело-финская лайка'), ('Карельская лайка', 'Карельская лайка'), ('Карельская медвежья собака', 'Карельская медвежья собака'), ('Карликовый пинчер', 'Карликовый пинчер'), ('Каталонская овчарка', 'Каталонская овчарка'), ('Кеесхонд', 'Кеесхонд'), ('Керн-терьер', 'Керн-терьер'), ('Керри-блю-терьер', 'Керри-блю-терьер'), ('Кинг-чарльз-спаниель', 'Кинг-чарльз-спаниель'), ('Кисю (порода собак)', 'Кисю (порода собак)'), ('Китайская хохлатая собака', 'Китайская хохлатая собака'), ('Кламбер-спаниель', 'Кламбер-спаниель'), ('Коикерхондье', 'Коикерхондье'), ('Комондор', 'Комондор'), ('Континентальный бульдог', 'Континентальный бульдог'), ('Континентальный той-спаниель', 'Континентальный той-спаниель'), ('Корейский чиндо', 'Корейский чиндо'), ('Короткошёрстный колли', 'Короткошёрстный колли'), ('Котон-де-тулеар', 'Котон-де-тулеар'), ('Крашская овчарка', 'Крашская овчарка'), ('Кромфорлендер', 'Кромфорлендер'), ('Ксолоитцкуинтли', 'Ксолоитцкуинтли'), ('Кубинский дог', 'Кубинский дог'), ('Кувас', 'Кувас'), ('Кури', 'Кури'), ('Курцхаар', 'Курцхаар'), ('Курчавошёрстный ретривер', 'Курчавошёрстный ретривер'), ('Лабрадор-ретривер', 'Лабрадор-ретривер'), ('Лабрадудль', 'Лабрадудль'), ('Лаготто-романьоло', 'Лаготто-романьоло'), ('Лангхаар', 'Лангхаар'), ('Ландсир', 'Ландсир'), ('Ланкаширский хилер', 'Ланкаширский хилер'), ('Левретка', 'Левретка'), ('Лейкленд-терьер', 'Лейкленд-терьер'), ('Леонбергер', 'Леонбергер'), ('Леопардовая собака Катахулы', 'Леопардовая собака Катахулы'), ('Лопарская оленегонная собака', 'Лопарская оленегонная собака'), ('Лхаса апсо', 'Лхаса апсо'), ('Майоркская овчарка', 'Майоркская овчарка'), ('Малая львиная собака', 'Малая львиная собака'), ('Малая швейцарская гончая', 'Малая швейцарская гончая'), ('Малые бельгийские собаки', 'Малые бельгийские собаки'), ('Малый вандейский бассет-гриффон', 'Малый вандейский бассет-гриффон'), ('Мальтезе Мальтийская болонка', 'Мальтезе Мальтийская болонка'), ('', ''), ('Манчестер-терьер', 'Манчестер-терьер'), ('Мареммо-абруццкая овчарка', 'Мареммо-абруццкая овчарка'), ('Махореро', 'Махореро'), ('Меделянка', 'Меделянка'), ('Миттельшнауцер', 'Миттельшнауцер'), ('Мопс', 'Мопс'), ('Московская сторожевая', 'Московская сторожевая'), ('Муди', 'Муди'), ('Неаполитанский мастиф', 'Неаполитанский мастиф'), ('Немецкая овчарка', 'Немецкая овчарка'), ('Немецкий боксёр', 'Немецкий боксёр'), ('Немецкий вахтельхунд', 'Немецкий вахтельхунд'), ('Немецкий дог', 'Немецкий дог'), ('Немецкий пинчер', 'Немецкий пинчер'), ('Немецкий шпиц', 'Немецкий шпиц'), ('Немецкий ягдтерьер', 'Немецкий ягдтерьер'), ('Ненецкая лайка', 'Ненецкая лайка'), ('Новошотландский ретривер', 'Новошотландский ретривер'), ('Норботтен шпиц', 'Норботтен шпиц'), ('Норвежский бухунд', 'Норвежский бухунд'), ('Норвежский лундехунд', 'Норвежский лундехунд'), ('Норвежский серый элкхунд', 'Норвежский серый элкхунд'), ('Норвежский чёрный элкхунд', 'Норвежский чёрный элкхунд'), ('Норвич-терьер', 'Норвич-терьер'), ('Норфолк-терьер', 'Норфолк-терьер'), ('Ньюфаундленд', 'Ньюфаундленд'), ('Одис', 'Одис'), ('Оттерхаунд', 'Оттерхаунд'), ('Пагль', 'Пагль'), ('Папийон', 'Папийон'), ('Парсон-рассел-терьер', 'Парсон-рассел-терьер'), ('Паттердейл-терьер', 'Паттердейл-терьер'), ('Пекинес', 'Пекинес'), ('Перуанская голая собака', 'Перуанская голая собака'), ('Пикардийская овчарка', 'Пикардийская овчарка'), ('Пиренейская горная собака', 'Пиренейская горная собака'), ('Пиренейская овчарка', 'Пиренейская овчарка'), ('Пиренейский мастиф', 'Пиренейский мастиф'), ('Поденко ибиценко', 'Поденко ибиценко'), ('Поденко канарио', 'Поденко канарио'), ('Польская гончая', 'Польская гончая'), ('Польская низинная овчарка', 'Польская низинная овчарка'), ('Польская подгалянская овчарка', 'Польская подгалянская овчарка'), ('Польский огар', 'Польский огар'), ('Померанский шпиц', 'Померанский шпиц'), ('Португальская водяная собака', 'Португальская водяная собака'), ('Португальская овчарка', 'Португальская овчарка'), ('Португальский поденгу', 'Португальский поденгу'), ('Пражский крысарик', 'Пражский крысарик'), ('Прямошёрстный ретривер', 'Прямошёрстный ретривер'), ('Пти-брабансон', 'Пти-брабансон'), ('Пудель', 'Пудель'), ('Пули', 'Пули'), ('Пуми (порода собак)', 'Пуми (порода собак)'), ('Пхунсан', 'Пхунсан'), ('Раджапалайям (порода собак)', 'Раджапалайям (порода собак)'), ('Ризеншнауцер', 'Ризеншнауцер'), ('Родезийский риджбек', 'Родезийский риджбек'), ('Ротвейлер', 'Ротвейлер'), ('Румынская карпатская овчарка', 'Румынская карпатская овчарка'), ('Румынская миоритская овчарка', 'Румынская миоритская овчарка'), ('Русская гончая', 'Русская гончая'), ('Русская псовая борзая', 'Русская псовая борзая'), ('Русская цветная болонка', 'Русская цветная болонка'), ('Русский охотничий спаниель', 'Русский охотничий спаниель'), ('Русский той', 'Русский той'), ('Русско-европейская лайка', 'Русско-европейская лайка'), ('Рюкю (порода собак)', 'Рюкю (порода собак)'), ('Салюки', 'Салюки'), ('Самоедская собака', 'Самоедская собака'), ('Сахалинский хаски', 'Сахалинский хаски'), ('Северная Инуитская собака', 'Северная Инуитская собака'), ('Сенбернар', 'Сенбернар'), ('Сиба-ину', 'Сиба-ину'), ('Сибирский хаски', 'Сибирский хаски'), ('Сикоку (порода собак)', 'Сикоку (порода собак)'), ('Силихем-терьер', 'Силихем-терьер'), ('Скайтерьер', 'Скайтерьер'), ('Словацкий копов', 'Словацкий копов'), ('Словацкий чувач', 'Словацкий чувач'), ('Слюги', 'Слюги'), ('Среднеазиатская овчарка', 'Среднеазиатская овчарка'), ('Староанглийский бульдог', 'Староанглийский бульдог'), ('Староанглийский бульдог (заново созданный)', 'Староанглийский бульдог (заново созданный)'), ('Стаффордширский бультерьер', 'Стаффордширский бультерьер'), ('Суссекс-спаниель', 'Суссекс-спаниель'), ('Схипперке', 'Схипперке'), ('Тазы (порода собак)', 'Тазы (порода собак)'), ('Тайваньская собака', 'Тайваньская собака'), ('Тайган (порода собак)', 'Тайган (порода собак)'), ('Тайский бангку', 'Тайский бангку'), ('Тайский риджбек', 'Тайский риджбек'), ('Такса', 'Такса'), ('Течичи', 'Течичи'), ('Тибетский мастиф', 'Тибетский мастиф'), ('Тибетский спаниель', 'Тибетский спаниель'), ('Тибетский терьер', 'Тибетский терьер'), ('Торньяк', 'Торньяк'), ('Тоса-ину', 'Тоса-ину'), ('Уиппет', 'Уиппет'), ('Фален', 'Фален'), ('Фараонова собака', 'Фараонова собака'), ('Фарфоровая гончая', 'Фарфоровая гончая'), ('Финская гончая', 'Финская гончая'), ('Финский лаппхунд', 'Финский лаппхунд'), ('Финский шпиц', 'Финский шпиц'), ('Фландрский бувье', 'Фландрский бувье'), ('Фокстерьер', 'Фокстерьер'), ('Французский бульдог', 'Французский бульдог'), ('Ханаанская собака', 'Ханаанская собака'), ('Харьер', 'Харьер'), ('Хеллефорсхунд', 'Хеллефорсхунд'), ('Ховаварт', 'Ховаварт'), ('Хоккайдо', 'Хоккайдо'), ('Хорватская овчарка', 'Хорватская овчарка'), ('Цвергпинчер', 'Цвергпинчер'), ('Цвергшнауцер', 'Цвергшнауцер'), ('Чау-чау', 'Чау-чау'), ('Чёрный терьер', 'Чёрный терьер'), ('Чесапик-бей-ретривер', 'Чесапик-бей-ретривер'), ('Чехословацкая волчья собака', 'Чехословацкая волчья собака'), ('Чешская пастушья собака', 'Чешская пастушья собака'), ('Чешский терьер', 'Чешский терьер'), ('Чинук', 'Чинук'), ('Чирнеко дель Этна', 'Чирнеко дель Этна'), ('Чихуахуа', 'Чихуахуа'), ('Чукотская ездовая', 'Чукотская ездовая'), ('Шапендуа', 'Шапендуа'), ('Шарпей', 'Шарпей'), ('Шарпланинская овчарка', 'Шарпланинская овчарка'), ('Шведский белый элкхунд', 'Шведский белый элкхунд'), ('Шведский вальхунд', 'Шведский вальхунд'), ('Шведский лаппхунд', 'Шведский лаппхунд'), ('Швейцарская гончая', 'Швейцарская гончая'), ('Шелковистый виндхаунд', 'Шелковистый виндхаунд'), ('Шелти', 'Шелти'), ('Ши-тцу', 'Ши-тцу'), ('Шотландский сеттер', 'Шотландский сеттер'), ('Шотландский терьер', 'Шотландский терьер'), ('Энтлебухер зенненхунд', 'Энтлебухер зенненхунд'), ('Эрдельтерьер', 'Эрдельтерьер'), ('Эстонская гончая', 'Эстонская гончая'), ('Эштрельская овчарка', 'Эштрельская овчарка'), ('Южнорусская овчарка', 'Южнорусская овчарка'), ('Якутская лайка', 'Якутская лайка'), ('Ямтхунд', 'Ямтхунд'), ('Японский терьер', 'Японский терьер'), ('Японский хин', 'Японский хин'), ('Японский шпиц', 'Японский шпиц')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.CharField(choices=[('Заводчик', 'Заводчик'), ('Приют', 'Приют')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(choices=[('Маленький', 'Маленький'), ('Средний', 'Средний'), ('Большой', 'Большой')], max_length=20),
        ),
    ]