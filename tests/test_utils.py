import pytest

from src.utils import conv_hh_vacancies, conv_sj_vacancies, format_hh_salary


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

