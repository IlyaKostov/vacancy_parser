import json
import os
import time
from abc import ABC, abstractmethod

import requests


class PlatformsAPI(ABC):

    @abstractmethod
    def get_vacancies(self, query):
        pass


class HeadHunterAPI(PlatformsAPI):

    URL = "https://api.hh.ru/vacancies"
    MAX_PAGES = 5

    def get_vacancies(self, query: str):
        """
        Получение списка вакансий с платформы HeadHunter
        :param query: текст запроса
        :return: list
        """
        vacancies_lst = []
        for page in range(self.MAX_PAGES):
            params = {'per_page': 100,
                      'page': page,
                      'text': query,
                      'search_field': 'name',
                      'order_by': "publication_time",
                      'area': [113, 16, 40],
                      }
            vacancies = requests.get(self.URL, params=params).json()
            vacancies_lst.extend(vacancies['items'])
            if (vacancies['pages'] - page) <= 1:
                break
            time.sleep(0.5)
        return vacancies_lst


class SuperJobAPI(PlatformsAPI):
    MAX_PAGES = 5
    URL = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.x_api_app_id = os.getenv('SUPER_JOB_API')

    def get_vacancies(self, query: str):
        """
        Получение списка вакансий с платформы SuperJob
        :param query: текст запроса
        :return: list
        """
        vacancies_lst = []
        for page in range(self.MAX_PAGES):

            headers = {
                       'X-Api-App-Id': self.x_api_app_id,
                       }
            params = {'keyword': query,
                      'page': page,
                      'count': 100,
                      'order_direction': 'desc',
                      }

            vacancies = requests.get(self.URL, headers=headers, params=params).json()
            try:
                vacancies_lst.extend(vacancies['objects'])
            except KeyError:
                return print(vacancies['error']['message'])
            else:
                if not vacancies['more']:
                    break
                time.sleep(0.5)
        return vacancies_lst
