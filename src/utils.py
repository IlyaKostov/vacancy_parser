import re

from src.api_classes import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()


def conv_hh_vacancies(vacancy_list: list) -> list:
    """
    Преобразование результатов запроса в список экземпляров класса Vacancy
    :param vacancy_list: list
    :return: list
    """
    converted_vacancies = []
    for elem in vacancy_list:
        title = elem['name']
        link = elem['alternate_url']
        salary = format_hh_salary(elem['salary'])
        area = elem['area']['name']
        description = f"{elem['snippet']['requirement']}\n{elem['snippet']['responsibility']}"
        clean_description = re.sub('<highlighttext>|</highlighttext>', '', description)
        converted_vacancy = Vacancy(title, link, salary, area, clean_description)
        converted_vacancies.append(converted_vacancy)
    return converted_vacancies


def format_hh_salary(salary: dict | None) -> str:
    """
    Форматирование блока зарплаты и валюты
    :param salary: item or None
    :return: str
    """
    if salary is None:
        return "Не указана"
    elif salary['to'] is None:
        currency = salary.get('currency')
        if currency == 'RUR':
            currency = 'руб.'
        elif currency == 'BYR':
            currency = 'бел. руб.'
        return f"от {salary['from']} {currency}"
    elif salary['from'] is None:
        currency = salary.get('currency')
        if currency == 'RUR':
            currency = 'руб.'
        elif currency == 'BYR':
            currency = 'бел. руб.'
        return f"до {salary['to']} {currency}"
    else:
        currency = salary.get('currency')
        if currency == 'RUR':
            currency = 'руб.'
        elif currency == 'BYR':
            currency = 'бел. руб.'
        return f"от {salary['from']} до {salary['to']} {currency}"


def conv_sj_vacancies(vacancy_list: list) -> list:
    """
        Преобразование результатов запроса в список экземпляров класса Vacancy
        :param vacancy_list: list
        :return: list
        """
    converted_vacancies = []
    for elem in vacancy_list:
        title = elem['profession']
        link = elem['link']
        salary_from = elem['payment_from']
        salary_to = elem['payment_to']
        currency = elem.get('currency')
        if currency == 'rub':
            currency = 'руб.'
        elif currency == 'uah':
            currency = 'грн.'
        elif currency == 'uzs':
            currency = 'сум'

        if salary_from == 0 and salary_to == 0:
            salary = "Не указана"
        elif salary_to == 0:
            salary = f"от {salary_from} {currency}"
        elif salary_from == 0:
            salary = f"до {salary_to} {currency}"
        elif salary_from == salary_to:
            salary = f"до {salary_to} {currency}"
        else:
            salary = f"от {salary_from} до {salary_to} руб."
        area = elem['town']['title']
        description = elem['candidat']
        converted_vacancy = Vacancy(title, link, salary, area, description)
        converted_vacancies.append(converted_vacancy)
    return converted_vacancies





# user_interaction()
# vacancies = Vacancy.all_vacancy
# vacancies.sort(reverse=True)
# print(*vacancies, sep='\n')
# print(conv_hh_vacancies(hh_api.get_vacancies('Python')))

