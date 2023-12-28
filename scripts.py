from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
from random import choice


CHOISE_OF_PRAISE = ["Молодец!", "Гораздо лучше, чем я ожидал!", "Сказано здорово – просто и ясно!",
                            "Уже существенно лучше!", "Очень хороший ответ!", "Так держать!"]


def get_schoolkid(schoolkid):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.DoesNotExist:
        print("Неправильно введены ФИО ученика")
    except Schoolkid.MultipleObjectsReturned:
        print("Учеников в данным ФИО найдено более 1. Уточните данные.")


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject, choise_of_price=CHOISE_OF_PRAISE):
    random_lesson = Lesson.objects.filter(subject__title=subject, year_of_study=schoolkid.year_of_study,
                                    group_letter=schoolkid.group_letter).order_by('?').first()
    try:
        Commendation.objects.create(schoolkid=schoolkid, teacher=random_lesson.teacher,
                                               subject=random_lesson.subject, created=random_lesson.date,
                                               text=choice(choise_of_price))
    except IndexError:
        print("Неправильно введен предмет")