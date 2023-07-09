class Vacancy:
    all_vacancy = []

    def __init__(self, title: str, link: str, salary: int | str, area: str, description: str) -> None:
        self.__check(title, link, salary, area, description)

        self.__title = title
        self.__link = link
        self.__salary = salary
        self.__area = area
        self.__description = description
        self.all_vacancy.append(self)

    def __str__(self):
        return f'Вакансия: {self.__title} ' \
               f'Ссылка на вакансию: {self.__link}\n' \
               f'Зарплата: {self.__salary} ' \
               f'Город: {self.__area}\n' \
               f'Описание: {self.__description}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__title}, {self.__link}, ' \
               f'{self.__salary}, {self.__area}, {self.__description})'

    @property
    def title(self):
        return self.__title

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def area(self):
        return self.__area

    @property
    def description(self):
        return self.__description

    @staticmethod
    def __check(title, link, salary, area, description):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError('Название вакансии должно быть непустой строкой')
        if not isinstance(link, str) or len(link.strip()) == 0:
            raise ValueError('Ссылка на вакансию должна быть непустой строкой')
        if not isinstance(salary, int | float) and not 'null':
            raise ValueError('Зарплата должна быть числом')
        if not isinstance(area, str) or len(area.strip()) == 0:
            raise ValueError('Название города должно быть непустой строкой')
        if not isinstance(description, str) or len(description.strip()) == 0:
            raise ValueError('Описание вакансии должно быть непустой строкой')

    def __eq__(self, other):
        return self.__salary == other.salary

    def __gt__(self, other):
        return self.__salary > other.salary

    def __lt__(self, other):
        return self.__salary < int(other.salary)

# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Moscow",
#                   "Требования: опыт работы от 3 лет...")

# # vacancy.title = '123'
# vacancy.link = '234'
# print(vacancy.link)
