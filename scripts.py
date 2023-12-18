from datacenter.models import *
from random import choice

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2, 3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(schoolkid, subject):
    try:
        choice_of_praise = ["Молодец!", "Гораздо лучше, чем я ожидал!", "Сказано здорово – просто и ясно!",
                            "Уже существенно лучше!", "Очень хороший ответ!", "Так держать!"]
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
        lessons = Lesson.objects.filter(subject__title=subject, year_of_study=schoolkid.year_of_study,
                                        group_letter=schoolkid.group_letter).order_by('-date')
        random_lesson = choice(lessons)
        Commendation.objects.create(schoolkid=schoolkid, teacher=random_lesson.teacher,
                                                   subject=random_lesson.subject, created=random_lesson.date,
                                                   text=choice(choice_of_praise))
    except ObjectDoesNotExist:
        print("Неправильно введены ФИО ученика")
    except MultipleObjectsReturned:
        print("Учеников в данным ФИО найдено более 1. Уточните данные.")
    except IndexError:
        print("Неправильно введен предмет")
