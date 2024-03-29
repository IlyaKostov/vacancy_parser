from src.utils import hh_api, conv_hh_vacancies, sj_api, conv_sj_vacancies, \
    get_search_query_and_top_n, process_vacancies, process_converted_and_filtered


def user_interaction():
    while True:
        try:
            choose_platform = int(input('Выберите платформу по которой хотите осуществлять поиск:\n'
                                        '1 - HeadHunter\n2 - SuperJob\n3 - искать на всех платформах\n'
                                        '4 - Выйти\n'))
        except ValueError:
            print('Нужно вводить число, попробуй снова')
            continue
        if choose_platform == 1:
            try:
                search_query, top_n, filter_word = get_search_query_and_top_n()
            except ValueError:
                print('Нужно вводить число, попробуй снова')
                continue
            vacancy_list = hh_api.get_vacancies(search_query)
            convert_vacancies = conv_hh_vacancies(vacancy_list)
            print(f'По вашему запросу найдено вакансий: {len(convert_vacancies)}')
            if len(convert_vacancies) == 0:
                print('\nТаких вакансий не существует. Попробуй еще раз\n')
                continue
            filtered_vacancies = process_converted_and_filtered(convert_vacancies, filter_word)
            if not filtered_vacancies and len(convert_vacancies) != 0:
                print("Но к сожалению, нет вакансий соответствующих заданным критериям.\n")
                continue

            process_vacancies(filtered_vacancies, top_n)

        elif choose_platform == 2:
            try:
                search_query, top_n, filter_word = get_search_query_and_top_n()
            except ValueError:
                print('Нужно вводить число, попробуй снова')
                continue
            vacancy_list = sj_api.get_vacancies(search_query)
            convert_vacancies = conv_sj_vacancies(vacancy_list)
            print(f'По вашему запросу найдено вакансий: {len(convert_vacancies)}')
            if len(convert_vacancies) == 0:
                print('\nТаких вакансий не существует. Попробуй еще раз\n')
                continue
            filtered_vacancies = process_converted_and_filtered(convert_vacancies, filter_word)
            if not filtered_vacancies and len(convert_vacancies) != 0:
                print("Но к сожалению, нет вакансий соответствующих заданным критериям.\n")
                continue
            process_vacancies(filtered_vacancies, top_n)

        elif choose_platform == 3:
            try:
                search_query, top_n, filter_word = get_search_query_and_top_n()
            except ValueError:
                print('Нужно вводить число, попробуй снова')
                continue
            vacancy_list_hh = hh_api.get_vacancies(search_query)
            vacancy_list_sj = sj_api.get_vacancies(search_query)
            convert_vacancies = conv_hh_vacancies(vacancy_list_hh) + conv_sj_vacancies(vacancy_list_sj)
            print(f'По вашему запросу найдено вакансий: {len(convert_vacancies)}')
            if len(convert_vacancies) == 0:
                print('\nТаких вакансий не существует. Попробуй еще раз\n')
                continue
            filtered_vacancies = process_converted_and_filtered(convert_vacancies, filter_word)
            if not filtered_vacancies and len(convert_vacancies) != 0:
                print("Но к сожалению, нет вакансий соответствующих заданным критериям.\n")
                continue
            process_vacancies(filtered_vacancies, top_n)

        elif choose_platform == 4:
            break
        else:
            print('Такого варианта нет')


if __name__ == '__main__':
    user_interaction()
