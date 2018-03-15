# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180120_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='photo',
            field=models.ImageField(default='..defaultpic.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='dog',
            name='photo',
            field=models.ImageField(default='..defaultpic.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(choices=[('no', 'Без породы'), ('0', 'Абиссинская'), ('1', 'Австралийский мист'), ('2', 'Азиатская (Табби)'), ('3', 'Акринская'), ('4', 'Американская жесткошёрстная'), ('5', 'Американская короткошёрстная'), ('6', 'Американский бобтейл длинношёрстный'), ('7', 'Американский бобтейл короткошёрстный'), ('8', 'Американский кёрл длинношёрстный'), ('9', 'Американский кёрл короткошёрстный'), ('10', 'Анатолийская'), ('11', 'Аравийский мау'), ('12', 'Балинезийская (Балийская)'), ('13', 'Бенгальская'), ('14', 'Бомбейская'), ('15', 'Бразильская короткошёрстная'), ('16', 'Британская длинношёрстная'), ('17', 'Британская короткошёрстная'), ('18', 'Бурма (Бурманская)'), ('19', 'Бурмилла длинношёрстный'), ('20', 'Бурмилла короткошёрстный'), ('21', 'Гавана'), ('22', 'Гималайская кошка'), ('23', 'Девон рекс'), ('24', 'Домашняя'), ('25', 'Донской сфинкс'), ('26', 'Египетская мау'), ('27', 'Калифорнийская сияющая'), ('28', 'Канаани'), ('29', 'Карельский бобтейл длинношёрстный'), ('30', 'Карельский бобтейл короткошёрстный'), ('31', 'Кельтская (Европейская короткошёрстная)'), ('32', 'Кимрик'), ('33', 'Колорпойнт'), ('34', 'Корат'), ('35', 'Корниш рекс'), ('36', 'Курильский бобтейл длинношёрстный'), ('37', 'Курильский бобтейл короткошёрстный'), ('38', 'Лаперм длинношёрстный'), ('39', 'Лаперм короткошёрстный'), ('40', 'Манчкин длинношёрстная'), ('41', 'Манчкин короткошёрстная'), ('42', 'Мейн-кун'), ('43', 'Меконгский бобтейл'), ('44', 'Минскин'), ('45', 'Мэнкс (Мэнская кошка)'), ('46', 'Наполеон'), ('47', 'Невская маскарадная'), ('48', 'Немецкий рекс'), ('49', 'Нибелунг'), ('50', 'Норвежская лесная'), ('51', 'Орегон-рекс'), ('52', 'Ориентальная длинношёрстная'), ('53', 'Ориентальная короткошёрстная'), ('54', 'Охос азулес'), ('55', 'Охос азулес длинношёрстный'), ('56', 'Оцикет'), ('57', 'Персидская (Колорпойнт)'), ('58', 'Петерболд'), ('59', 'Пиксибоб длинношёрстный'), ('60', 'Пиксибоб короткошёрстный'), ('61', 'Рагамаффин'), ('62', 'Русская голубая'), ('63', 'Рэгдолл'), ('64', 'Саванна'), ('65', 'Священная бирманская'), ('66', 'Сейшельская длинношёрстная'), ('67', 'Сейшельская короткошёрстная'), ('68', 'Селкирк рекс длинношёрстный'), ('69', 'Селкирк рекс короткошёрстный'), ('70', 'Серенгети'), ('71', 'Сиамская'), ('72', 'Сибирская'), ('73', 'Сингапурская'), ('74', 'Скоттиш страйт'), ('75', 'Скоттиш фолд'), ('76', 'Сноу-Шу'), ('77', 'Сококе'), ('78', 'Сомали'), ('79', 'Сфинкс (Канадский)'), ('80', 'Тайская'), ('81', 'Тойгер'), ('82', 'Тонкинская'), ('83', 'Турецкая ангора'), ('84', 'Турецкий ван'), ('85', 'Украинский левкой'), ('86', 'Уральский рекс длинношёрстный'), ('87', 'Уральский рекс короткошёрстный'), ('88', 'Форин Вайт'), ('89', 'Хайленд фолд'), ('90', 'Цейлонская'), ('91', 'Чаузи'), ('92', 'Шантильи Тиффаны'), ('93', 'Шартрез'), ('94', 'Эгейская'), ('95', 'Экзотическая'), ('96', 'Экспериментальная порода'), ('97', 'Яванез (Яванская)'), ('98', 'Японский бобтейл длинношёрстный'), ('99', 'Японский бобтейл короткошёрстный')], default='не указан', max_length=4),
        ),
        migrations.AlterField(
            model_name='cat',
            name='city',
            field=models.CharField(default='не указан', max_length=100),
        ),
        migrations.AlterField(
            model_name='cat',
            name='competition',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.CharField(choices=[('none', 'не указан'), ('alone', 'заводчик'), ('adopt', 'приют')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='cat',
            name='parent_competition',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cat',
            name='passport',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(choices=[('none', 'не указан'), ('male', 'мальчик'), ('female', 'девочка')], default='не указан', max_length=6),
        ),
        migrations.AlterField(
            model_name='cat',
            name='size',
            field=models.CharField(choices=[('none', 'не указан'), ('small', 'маленький'), ('average', 'средний'), ('big', 'большой')], default='не указан', max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(choices=[('no', 'Без породы'), ('0', 'Австралийская короткохвостая пастушья собака'), ('1', 'Австралийская овчарка'), ('2', 'Австралийская пастушья собака'), ('3', 'Австралийский келпи'), ('4', 'Австралийский терьер'), ('5', 'Австралийский шелковистый терьер'), ('6', 'Австрийская гончая'), ('7', 'Австрийский брудастый бракк'), ('8', 'Австрийский пинчер'), ('9', 'Азавак'), ('10', 'Азорская пастушья собака'), ('11', 'Аиди'), ('12', 'Акита-ину'), ('13', 'Алан'), ('14', 'Алано'), ('15', 'Алапахский бульдог'), ('16', 'Альпийская таксообразная гончая'), ('17', 'Аляскинский кли-кай'), ('18', 'Аляскинский маламут'), ('19', 'Американская акита'), ('20', 'Американская эскимосская собака'), ('21', 'Американский бандог'), ('22', 'Американский бульдог'), ('23', 'Американский водяной спаниель'), ('24', 'Американский голый терьер'), ('25', 'Американский кокер-спаниель'), ('26', 'Американский мастиф'), ('27', 'Американский питбультерьер'), ('28', 'Американский стаффордширский терьер'), ('29', 'Американский фоксхаунд'), ('30', 'Анатолийская овчарка'), ('31', 'Английская енотовая гончая'), ('32', 'Английская овчарка'), ('33', 'Английский бульдог'), ('34', 'Английский водяной спаниель'), ('35', 'Английский кокер-спаниель'), ('36', 'Английский мастиф'), ('37', 'Английский пойнтер'), ('38', 'Английский сеттер'), ('39', 'Английский спрингер-спаниель'), ('40', 'Английский той-терьер'), ('41', 'Английский фоксхаунд'), ('42', 'Англо-французская малая гончая'), ('43', 'Аппенцеллер зенненхунд'), ('44', 'Аргентинский дог'), ('45', 'Арденнский бувье'), ('46', 'Артуазская гончая'), ('47', 'Афганская борзая'), ('48', 'Аффенпинчер'), ('49', 'Баварская горная гончая'), ('50', 'Бакхмуль'), ('51', 'Барбет (собака)'), ('52', 'Басенджи'), ('53', 'Баскская овчарка'), ('54', 'Бассет-хаунд'), ('55', 'Бедлингтон-терьер'), ('56', 'Белая швейцарская овчарка'), ('57', 'Бельгийская овчарка'), ('58', 'Бельгийский гриффон'), ('59', 'Бергамская овчарка'), ('60', 'Бернская гончая'), ('61', 'Бернский зенненхунд'), ('62', 'Бивер-йоркширский терьер'), ('63', 'Бигль'), ('64', 'Бишон фризе'), ('65', 'Бладхаунд'), ('66', 'Блю-лейси'), ('67', 'Бобтейл'), ('68', 'Болгарский барак'), ('69', 'Болоньез'), ('70', 'Большой вандейский бассет-гриффон'), ('71', 'Большой вандейский гриффон'), ('72', 'Большой швейцарский зенненхунд'), ('73', 'Бордер-колли'), ('74', 'Бордер-терьер'), ('75', 'Бордоский дог'), ('76', 'Бородатый колли'), ('77', 'Босерон'), ('78', 'Бостон-терьер'), ('79', 'Бразильский терьер'), ('80', 'Бразильский фила'), ('81', 'Бретонский эпаньоль'), ('82', 'Бриар (порода собак)'), ('83', 'Брохольмер'), ('84', 'Брюссельский гриффон'), ('85', 'Буковинская овчарка'), ('86', 'Бульдог кампейро'), ('87', 'Бульдог Катахулы'), ('88', 'Бульмастиф'), ('89', 'Бультерьер'), ('90', 'Бурбуль'), ('91', 'Бурят-монгольский волкодав'), ('92', 'Валенсийский ратер'), ('93', 'Вандейский бассет-гриффон'), ('94', 'Веймаранер'), ('95', 'Вельш-корги'), ('96', 'Вельш-спрингер-спаниель'), ('97', 'Вельштерьер'), ('98', 'Венгерская выжла'), ('99', 'Вертельная собака'), ('100', 'Вест-хайленд-уайт-терьер'), ('101', 'Веттерхун'), ('102', 'Волчья собака Сарлоса'), ('103', 'Вольпино итальяно'), ('104', 'Восточноевропейская овчарка'), ('105', 'Восточносибирская лайка'), ('106', 'Гаванский бишон'), ('107', 'Гамильтонстёваре'), ('108', 'Гампр'), ('109', 'Гладкошёрстный фокстерьер'), ('110', 'Глен оф Имаал терьер'), ('111', 'Голландская овчарка'), ('112', 'Голландский смоусхонд'), ('113', 'Голубой гасконский бассет'), ('114', 'Гончая Шиллера'), ('115', 'Грейхаунд'), ('116', 'Гренландская собака'), ('117', 'Греческая овчарка'), ('118', 'Грюнендаль'), ('119', 'Далматин'), ('120', 'Датско-шведская фермерская собака'), ('121', 'Денди-динмонт-терьер'), ('122', 'Джек-рассел-терьер'), ('123', 'Дзёмон-сиба'), ('124', 'Дирхаунд'), ('125', 'Длинношерстная акита-ину'), ('126', 'Длинношёрстный колли'), ('127', 'Доберман'), ('128', 'Дратхаар'), ('129', 'Древер'), ('130', 'Евразиер'), ('131', 'Жесткошёрстный фокстерьер'), ('132', 'Западносибирская лайка'), ('133', 'Золотистый ретривер'), ('134', 'Ирландский водяной спаниель'), ('135', 'Ирландский волкодав'), ('136', 'Ирландский красный сеттер'), ('137', 'Ирландский мягкошёрстный пшеничный терьер'), ('138', 'Ирландский терьер'), ('139', 'Исландская собака'), ('140', 'Испанская водяная собака'), ('141', 'Испанский гальго'), ('142', 'Испанский мастиф'), ('143', 'Итальянский бракк'), ('144', 'Итальянский спиноне'), ('145', 'Йоркширский терьер'), ('146', 'Ка-де-бо'), ('147', 'Кавалер-кинг-чарльз-спаниель'), ('148', 'Кавказская овчарка'), ('149', 'Каи (порода собак)'), ('150', 'Канарский дог'), ('151', 'Кане-корсо'), ('152', 'Као де кастро-лаборейро'), ('153', 'Каракачанская собака'), ('154', 'Карело-финская лайка'), ('155', 'Карельская лайка'), ('156', 'Карельская медвежья собака'), ('157', 'Карликовый пинчер'), ('158', 'Каталонская овчарка'), ('159', 'Кеесхонд'), ('160', 'Керн-терьер'), ('161', 'Керри-блю-терьер'), ('162', 'Кинг-чарльз-спаниель'), ('163', 'Кисю (порода собак)'), ('164', 'Китайская хохлатая собака'), ('165', 'Кламбер-спаниель'), ('166', 'Коикерхондье'), ('167', 'Комондор'), ('168', 'Континентальный бульдог'), ('169', 'Континентальный той-спаниель'), ('170', 'Корейский чиндо'), ('171', 'Короткошёрстный колли'), ('172', 'Котон-де-тулеар'), ('173', 'Крашская овчарка'), ('174', 'Кромфорлендер'), ('175', 'Ксолоитцкуинтли'), ('176', 'Кубинский дог'), ('177', 'Кувас'), ('178', 'Кури'), ('179', 'Курцхаар'), ('180', 'Курчавошёрстный ретривер'), ('181', 'Лабрадор-ретривер'), ('182', 'Лабрадудль'), ('183', 'Лаготто-романьоло'), ('184', 'Лангхаар'), ('185', 'Ландсир'), ('186', 'Ланкаширский хилер'), ('187', 'Левретка'), ('188', 'Лейкленд-терьер'), ('189', 'Леонбергер'), ('190', 'Леопардовая собака Катахулы'), ('191', 'Лопарская оленегонная собака'), ('192', 'Лхаса апсо'), ('193', 'Майоркская овчарка'), ('194', 'Малая львиная собака'), ('195', 'Малая швейцарская гончая'), ('196', 'Малые бельгийские собаки'), ('197', 'Малый вандейский бассет-гриффон'), ('198', 'Мальтезе Мальтийская болонка'), ('199', ''), ('200', 'Манчестер-терьер'), ('201', 'Мареммо-абруццкая овчарка'), ('202', 'Махореро'), ('203', 'Меделянка'), ('204', 'Миттельшнауцер'), ('205', 'Мопс'), ('206', 'Московская сторожевая'), ('207', 'Муди'), ('208', 'Неаполитанский мастиф'), ('209', 'Немецкая овчарка'), ('210', 'Немецкий боксёр'), ('211', 'Немецкий вахтельхунд'), ('212', 'Немецкий дог'), ('213', 'Немецкий пинчер'), ('214', 'Немецкий шпиц'), ('215', 'Немецкий ягдтерьер'), ('216', 'Ненецкая лайка'), ('217', 'Новошотландский ретривер'), ('218', 'Норботтен шпиц'), ('219', 'Норвежский бухунд'), ('220', 'Норвежский лундехунд'), ('221', 'Норвежский серый элкхунд'), ('222', 'Норвежский чёрный элкхунд'), ('223', 'Норвич-терьер'), ('224', 'Норфолк-терьер'), ('225', 'Ньюфаундленд'), ('226', 'Одис'), ('227', 'Оттерхаунд'), ('228', 'Пагль'), ('229', 'Папийон'), ('230', 'Парсон-рассел-терьер'), ('231', 'Паттердейл-терьер'), ('232', 'Пекинес'), ('233', 'Перуанская голая собака'), ('234', 'Пикардийская овчарка'), ('235', 'Пиренейская горная собака'), ('236', 'Пиренейская овчарка'), ('237', 'Пиренейский мастиф'), ('238', 'Поденко ибиценко'), ('239', 'Поденко канарио'), ('240', 'Польская гончая'), ('241', 'Польская низинная овчарка'), ('242', 'Польская подгалянская овчарка'), ('243', 'Польский огар'), ('244', 'Померанский шпиц'), ('245', 'Португальская водяная собака'), ('246', 'Португальская овчарка'), ('247', 'Португальский поденгу'), ('248', 'Пражский крысарик'), ('249', 'Прямошёрстный ретривер'), ('250', 'Пти-брабансон'), ('251', 'Пудель'), ('252', 'Пули'), ('253', 'Пуми (порода собак)'), ('254', 'Пхунсан'), ('255', 'Раджапалайям (порода собак)'), ('256', 'Ризеншнауцер'), ('257', 'Родезийский риджбек'), ('258', 'Ротвейлер'), ('259', 'Румынская карпатская овчарка'), ('260', 'Румынская миоритская овчарка'), ('261', 'Русская гончая'), ('262', 'Русская псовая борзая'), ('263', 'Русская цветная болонка'), ('264', 'Русский охотничий спаниель'), ('265', 'Русский той'), ('266', 'Русско-европейская лайка'), ('267', 'Рюкю (порода собак)'), ('268', 'Салюки'), ('269', 'Самоедская собака'), ('270', 'Сахалинский хаски'), ('271', 'Северная Инуитская собака'), ('272', 'Сенбернар'), ('273', 'Сиба-ину'), ('274', 'Сибирский хаски'), ('275', 'Сикоку (порода собак)'), ('276', 'Силихем-терьер'), ('277', 'Скайтерьер'), ('278', 'Словацкий копов'), ('279', 'Словацкий чувач'), ('280', 'Слюги'), ('281', 'Среднеазиатская овчарка'), ('282', 'Староанглийский бульдог'), ('283', 'Староанглийский бульдог (заново созданный)'), ('284', 'Стаффордширский бультерьер'), ('285', 'Суссекс-спаниель'), ('286', 'Схипперке'), ('287', 'Тазы (порода собак)'), ('288', 'Тайваньская собака'), ('289', 'Тайган (порода собак)'), ('290', 'Тайский бангку'), ('291', 'Тайский риджбек'), ('292', 'Такса'), ('293', 'Течичи'), ('294', 'Тибетский мастиф'), ('295', 'Тибетский спаниель'), ('296', 'Тибетский терьер'), ('297', 'Торньяк'), ('298', 'Тоса-ину'), ('299', 'Уиппет'), ('300', 'Фален'), ('301', 'Фараонова собака'), ('302', 'Фарфоровая гончая'), ('303', 'Финская гончая'), ('304', 'Финский лаппхунд'), ('305', 'Финский шпиц'), ('306', 'Фландрский бувье'), ('307', 'Фокстерьер'), ('308', 'Французский бульдог'), ('309', 'Ханаанская собака'), ('310', 'Харьер'), ('311', 'Хеллефорсхунд'), ('312', 'Ховаварт'), ('313', 'Хоккайдо'), ('314', 'Хорватская овчарка'), ('315', 'Цвергпинчер'), ('316', 'Цвергшнауцер'), ('317', 'Чау-чау'), ('318', 'Чёрный терьер'), ('319', 'Чесапик-бей-ретривер'), ('320', 'Чехословацкая волчья собака'), ('321', 'Чешская пастушья собака'), ('322', 'Чешский терьер'), ('323', 'Чинук'), ('324', 'Чирнеко дель Этна'), ('325', 'Чихуахуа'), ('326', 'Чукотская ездовая'), ('327', 'Шапендуа'), ('328', 'Шарпей'), ('329', 'Шарпланинская овчарка'), ('330', 'Шведский белый элкхунд'), ('331', 'Шведский вальхунд'), ('332', 'Шведский лаппхунд'), ('333', 'Швейцарская гончая'), ('334', 'Шелковистый виндхаунд'), ('335', 'Шелти'), ('336', 'Ши-тцу'), ('337', 'Шотландский сеттер'), ('338', 'Шотландский терьер'), ('339', 'Энтлебухер зенненхунд'), ('340', 'Эрдельтерьер'), ('341', 'Эстонская гончая'), ('342', 'Эштрельская овчарка'), ('343', 'Южнорусская овчарка'), ('344', 'Якутская лайка'), ('345', 'Ямтхунд'), ('346', 'Японский терьер'), ('347', 'Японский хин'), ('348', 'Японский шпиц')], default='не указан', max_length=4),
        ),
        migrations.AlterField(
            model_name='dog',
            name='city',
            field=models.CharField(default='не указан', max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='competition',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.CharField(choices=[('none', 'не указан'), ('alone', 'заводчик'), ('adopt', 'приют')], default='не указан', max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='parent_competition',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dog',
            name='passport',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dog',
            name='price',
            field=models.IntegerField(default='не указан'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(choices=[('none', 'не указан'), ('male', 'мальчик'), ('female', 'девочка')], default='не указан', max_length=6),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(choices=[('none', 'не указан'), ('small', 'маленький'), ('average', 'средний'), ('big', 'большой')], default='не указан', max_length=10),
        ),
    ]
