# Курсовой проект по ООП “Парсер вакансий”

---


### *В этом проекте написан парсер для сайтов вакансий hh.ru и superjob.ru*
 
1. Реализованы классы для работы с платформами hh.ru и superjob.ru
2. Реализован класс для работы с вакансиями, принимающий атрибуты такие как название вакансии, 
ссылка на вакансию, зарплата, город, краткое описание.
3. Создан класс для сохранения информации о вакансиях в JSON-файл, а также реализованы методы
класса для добавления вакансий в файл, получения данных из файла по указанным критериям 
и удаления информации о вакансиях

---

#### Определен сценарий взаимодействия с пользователем. 

- Предоставляется выбор платформы для поиска
- Запрашивается ключевое слово для поиска
- Запрашивается необходимый топ вакансий для вывода
- Предоставляется выбор о необходимости сортировки вакансий по зарплате
- Так же выводится общее количество найденных вакансий по ключевому слову
- Предоставляется возможность отказаться от вывода топа вакансий, для просмотра всех
- Есть возможность указать дополнительный критерий поиска