import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "от 100000 до 150000 руб.", "Moscow",
                      "Требования: опыт работы от 3 лет...")
    return vacancy


def test_init(vacancy):
    assert vacancy.title == "Python Developer"
    assert vacancy.link == "<https://hh.ru/vacancy/123456>"
    assert vacancy.salary == "от 100000 до 150000 руб."
    assert vacancy.area == "Moscow"
    assert vacancy.description == "Требования: опыт работы от 3 лет..."
    Vacancy("", "https://hh.ru/", "Не указана", "Moscow", "Требования:")
    Vacancy("Python Developer", "", "Не указана", "Moscow", "Требования:")
    Vacancy("Python Developer", "https://hh.ru/", 0, "Moscow", "Требования:")
    Vacancy("Python Developer", "https://hh.ru/", "Не указана", "", "Требования:")
    Vacancy("Python Developer", "https://hh.ru/", "Не указана", "Moscow", "")

def test_attribute_error_title(vacancy):
    with pytest.raises(AttributeError):
        vacancy.title = "Python"


def test_attribute_error_link(vacancy):
    with pytest.raises(AttributeError):
        vacancy.link = "<https://hh.ru/"


def test_attribute_error_salary(vacancy):
    with pytest.raises(AttributeError):
        vacancy.salary = "10 руб."


def test_attribute_error_area(vacancy):
    with pytest.raises(AttributeError):
        vacancy.area = "New-York"


def test_attribute_error_description(vacancy):
    with pytest.raises(AttributeError):
        vacancy.description = "Требования:"


def test_eq_gt_lt(vacancy):
    vacancy2 = Vacancy("Python", "https://hh.ru/", "от 101000 до 100000 руб.", "Moscow", "Требования:")
    assert (vacancy < vacancy2) is True
    vacancy2 = Vacancy("Python", "https://hh.ru/", "от 50000 руб.", "Moscow", "Требования:")
    assert (vacancy > vacancy2) is True
    vacancy2 = Vacancy("Python", "https://hh.ru/", "до 100000 руб.", "Moscow", "Требования:")
    assert (vacancy == vacancy2) is True
    vacancy2 = Vacancy("Python", "https://hh.ru/", "Не указана", "Moscow", "Требования:")
    vacancy3 = Vacancy("Python", "https://hh.ru/", "Не указана", "Moscow", "Требования:")
    assert (vacancy3 == vacancy2) is True


def test_vacancy_str(vacancy):
    assert str(vacancy) == 'Вакансия: Python Developer Ссылка на вакансию: '\
                           '<https://hh.ru/vacancy/123456>\n'\
                           'Зарплата: от 100000 до 150000 руб. Город: Moscow\n'\
                           'Описание: Требования: опыт работы от 3 лет...'


def test_vacancy_repr(vacancy):
    assert repr(vacancy) == 'Vacancy(Python Developer, <https://hh.ru/vacancy/123456>, от 100000 до 150000 руб.,' \
                            ' Moscow, Требования: опыт работы от 3 лет...)'
