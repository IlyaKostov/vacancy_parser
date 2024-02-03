import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class AbstractVacancyDatabase(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        pass


class JSONSaver(AbstractVacancyDatabase):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancies: list) -> None:
        with open(self.filename, 'w', encoding='utf-8') as file:
            data = []
            for vacancy in vacancies:
                vacancy_dict = {'title': vacancy.title, 'link': vacancy.link,
                                'salary': vacancy.salary, 'area': vacancy.area,
                                'description': vacancy.description}
                if vacancy_dict not in data:
                    data.append(vacancy_dict)
            json.dump(data, file, ensure_ascii=False, indent=2)

    def get_vacancies_by_keyword(self, keyword: str) -> list:
        """Получаем нужные словари с вакансиями по ключевому слову"""
        vacancies = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            data_list = json.load(file)
            for vacancy in data_list:
                if keyword in vacancy['description'].lower():
                    vacancies.append(vacancy)
        return vacancies

    def get_vacancies_by_area(self, area):
        vacancies = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            data_list = json.load(file)
            for vacancy in data_list:
                if area in vacancy['area'].lower():
                    vacancies.append(vacancy)
        return vacancies

    # def get_vacancies_by_salary(self, salary):
    #     vacancies = []
    #     with open(self.filename, 'r') as file:
    #         data_list = json.load(file)
    #         for vacancy in data_list:
    #             if salary in vacancy['salary'].lower():
    #                 vacancies.append(vacancy)
    #     return vacancies

    def remove_vacancy(self, rem_vacancy):
        """Удаляем вакансию по названию"""
        lines_to_keep = []
        if rem_vacancy != 'all':
            with open(self.filename, 'r', encoding='utf-8') as file:
                data_list = json.load(file)
                for vacancy in data_list:
                    if rem_vacancy not in vacancy['title']:
                        lines_to_keep.append(vacancy)
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(lines_to_keep, file, ensure_ascii=False, indent=2)
        else:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=2)