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

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query: str):
        """
        Получение списка вакансий с платформы HeadHunter
        :param query: текст запроса
        :return: list
        """
        vacancies_lst = []
        for page in range(10):
            params = {'per_page': 100,
                      'page': page,
                      'text': query,
                      'search_field': 'name',
                      'order_by': "publication_time",
                      'area': [113, 16, 40],
                      }
            response = requests.get(self.url, params=params)
            vacancies = response.json()
            vacancies_lst.extend(vacancies['items'])
            if (vacancies['pages'] - page) <= 1:
                break
            time.sleep(0.5)
        return vacancies_lst


class SuperJobAPI(PlatformsAPI):
    x_api_app_id = os.getenv('SUPER_JOB_API')

    def get_vacancies(self, query: str):
        """
        Получение списка вакансий с платформы SuperJob
        :param query: текст запроса
        :return: list
        """
        vacancies_lst = []
        for page in range(10):

            headers = {
                       'X-Api-App-Id': self.x_api_app_id,
                       }
            url = 'https://api.superjob.ru/2.0/vacancies/'
            params = {'keyword': query,
                      'page': page,
                      'count': 100,
                      }

            vacancies = requests.get(url, headers=headers, params=params).json()
            vacancies_lst.extend(vacancies['objects'])
            if not vacancies['more']:
                break
            time.sleep(0.5)
        return vacancies_lst
