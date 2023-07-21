import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def json_saver():
    json_saver = JSONSaver('test.json')
    return json_saver


def test_json_saver_init(json_saver):
    assert json_saver.filename == 'test.json'


def test_add_vacancy(json_saver):
    json_saver.add_vacancy([Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                                    "Москва", "Требования: опыт работы от 3 лет...")])


def test_get_vacancies_by_keyword(json_saver):
    json_saver.get_vacancies_by_keyword('опыт')
