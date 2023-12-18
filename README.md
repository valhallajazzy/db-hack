# Скрипт по искправлению электронного дневника.

Данный код написан для электронного дневника написанном на Django, следовательно работает только 
в связке с ним. Ознакомиться с проектом можно [ЗДЕСЬ](https://github.com/devmanorg/e-diary/tree/master). Скрипт выполняет 3 функции:

* Исправление плохих оценок на 5 (функция fix_marks)
* Удаление замечаний от учителей (функция remove_chastisements)
* Создание хвалебных отзывов от учителей (функция create_commendation)

## Подготовка к запуску скрипта

* Скачиваем проект себе на ПК с [РЕПОЗИТОРИЯ](https://github.com/devmanorg/e-diary/tree/master) или подключаемся к запущенному серверу.
* Скачиваем скрипт и помещаем в корневую диреторию проекта

![Screenshot]()

* Из корневой директории проекта подключаемся в Django shell с помощью команды:

```console
$ python manage.py shell
```

* Импортируем модели в нашу рабочую среду командой `from datacenter.models import *`
* Импортируем функции скрипта в нашу рабочую среду `from scripts import *`

![Screenshot](https://github.com/valhallajazzy/db-hack/blob/main/pic_for_readme/shell.png)

## Запуск скрипта

### Исправление плохих оценок на 5 (функция fix_marks)

Для пользования этой функцией на нужно создать экземпляр модели ученика, оценки которого мы хотим исправить.

* Создадим его, заключив в переменную "schoolkid":
```console
  schoolkid = Schoolkid.objects.get(full_name__contains="<имя ученика>")
```
* Вызовем функцию, используя аргумент "schoolkid": `fix_marks(schoolkid)`
* Радуемся исправленным оценкам

Пример:

![Screenshot](https://github.com/valhallajazzy/db-hack/blob/main/pic_for_readme/fix_marks.png)

### Удаление замечаний от учителей (функция remove_chastisements)

Для пользования этой функцией на нужно создать экземпляр модели ученика, оценки которого мы хотим исправить.

* Создадим его, заключив в переменную "schoolkid":
```console
  schoolkid = Schoolkid.objects.get(full_name__contains="<имя ученика>")
```
* Вызовем функцию, используя аргумент "schoolkid": `remove_chastisements(schoolkid)`
* Радуемся удаленным замечаниям

Пример:

![Screenshot](https://github.com/valhallajazzy/db-hack/blob/main/pic_for_readme/remove_chastisements.png)

### Создание хвалебных отзывов от учителей (функция create_commendation)

Функция принимает два аргумента: schoolkid - <имя ученика>, subject - <предмет>

* Вызываем фунцкию прописывая аргументы: `create_commendation(schoolkid, subject)`
* Радуемся появившимся хвалебным отзывам

Пример:

![Screenshot](https://github.com/valhallajazzy/db-hack/blob/main/pic_for_readme/create_commendation.png)

