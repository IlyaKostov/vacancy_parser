import pytest

from src.utils import conv_hh_vacancies, conv_sj_vacancies, format_hh_salary, sort_vacancies, get_top_vacancies, \
    convert_vacancy
from src.vacancy import Vacancy


@pytest.fixture
def hh_vacancies_list():
    vacancies_list = [
        {
            "name": "Python разработчик",
            "area": {
                "name": "Москва",
            },
            "salary": {
                "from": 180000,
                "to": None,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/82299017",
            "snippet": {
                "requirement": "Наличие завершенных проектов в роли <highlighttext>разработчика</highlighttext>",
                "responsibility": "Разработка сервисов для middle-офиса компании – автоматизация ежедневных расчётов"
            },
        },
        {
            "name": "Python разработчик",
            "area": {
                "name": "Москва",
            },
            "salary": {
                "from": None,
                "to": 180000,
                "currency": "BYR",
            },
            "alternate_url": "https://hh.ru/vacancy/82299017",
            "snippet": {
                "requirement": "Наличие завершенных проектов в роли <highlighttext>разработчика</highlighttext>",
                "responsibility": "Разработка сервисов для middle-офиса компании – автоматизация ежедневных расчётов"
            },
        },
        {
            "name": "Python разработчик",
            "area": {
                "name": "Москва",
            },
            "salary": None,
            "alternate_url": "https://hh.ru/vacancy/82299017",
            "snippet": {
                "requirement": "Наличие завершенных проектов в роли <highlighttext>разработчика</highlighttext>",
                "responsibility": "Разработка сервисов для middle-офиса компании – автоматизация ежедневных расчётов"
            },
        },
    ]
    return vacancies_list


@pytest.fixture
def sj_vacancies_list():
    vacancies_list = [
        {
            "payment_from": 15000,
            "payment_to": 39000,
            "profession": "Специалист службы поддержки (Яндекс.Поиск)",
            "candidat": "Каждый день миллионы пользователей задают вопросы",
            "currency": "rub",
            "town": {
                "id": 4,
                "title": "Москва",
            },
            "link": "https://almetyevsk.superjob.ru/vakansii/specialist-sluzhby-podderzhki-45402326.html",
        },
        {
            "payment_from": 0,
            "payment_to": 39000,
            "profession": "Специалист службы поддержки (Яндекс.Поиск)",
            "candidat": "Каждый день миллионы пользователей задают вопросы",
            "currency": "uah",
            "town": {
                "id": 4,
                "title": "Москва",
            },
            "link": "https://almetyevsk.superjob.ru/vakansii/specialist-sluzhby-podderzhki-45402326.html",
        },
        {
            "payment_from": 0,
            "payment_to": 0,
            "profession": "Специалист службы поддержки (Яндекс.Поиск)",
            "candidat": "Каждый день миллионы пользователей задают вопросы",
            "currency": "uzs",
            "town": {
                "id": 4,
                "title": "Москва",
            },
            "link": "https://almetyevsk.superjob.ru/vakansii/specialist-sluzhby-podderzhki-45402326.html",
        }
    ]
    return vacancies_list


def test_conv_hh_vacancies(hh_vacancies_list):
    conv_hh_vacancies(hh_vacancies_list)


def test_conv_sj_vacancies(sj_vacancies_list):
    conv_sj_vacancies(sj_vacancies_list)


def test_format_hh_salary():
    assert format_hh_salary(None) == 'Не указана'
    assert format_hh_salary({"from": 180000,
                "to": None,
                "currency": "BYR",}) == "от 180000 бел. руб."
    assert format_hh_salary({"from": 180000,
                "to": 200000,
                "currency": "RUR",}) == "от 180000 до 200000 руб."
    assert format_hh_salary({"from": None,
                             "to": 200000,
                             "currency": "RUR", }) == "до 200000 руб."
    assert format_hh_salary({"from": 180000,
                             "to": 200000,
                             "currency": "BYR", }) == "от 180000 до 200000 бел. руб."


def test_sort_vacancies(hh_vacancies_list):
    vacancies = conv_hh_vacancies(hh_vacancies_list)
    assert sort_vacancies(vacancies) == [Vacancy("Python разработчик", "https://hh.ru/vacancy/82299017",
                                                 "от 180000 руб.", "Москва",
                                                 "Наличие завершенных проектов в роли разработчика\nРазработка сервисов "
                                                 "для middle-офиса компании – автоматизация ежедневных расчётов"),
                                         Vacancy("Python разработчик", "https://hh.ru/vacancy/82299017",
                                                 "до 180000 бел. руб.", "Москва",
                                                 "Наличие завершенных проектов в роли разработчика\nРазработка сервисов "
                                                 "для middle-офиса компании – автоматизация ежедневных расчётов"),
                                         Vacancy("Python разработчик", "https://hh.ru/vacancy/82299017", "Не указана",
                                                 "Москва", "Наличие завершенных проектов в роли разработчика\nРазработка "
                                                           "сервисов для middle-офиса компании – автоматизация ежедневных расчётов")]


def test_get_top_vacancies(hh_vacancies_list):
    vacancies = conv_hh_vacancies(hh_vacancies_list)
    top_n = 1
    get_top_vacancies(vacancies, top_n)


def test_convert_vacancy():
    data_list = [
    {
        "title": "Software Developer Python",
        "link": "https://hh.ru/vacancy/82595583",
        "salary": "от 80000 до 200000 руб.",
        "area": "Москва",
        "description": "Английский на уровне с"
    }
    ]
    assert convert_vacancy(data_list) == [Vacancy("Software Developer Python", "https://hh.ru/vacancy/82595583",
                                                  "от 80000 до 200000 руб.", "Москва",
                                                  "Английский на уровне с")]
