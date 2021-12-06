import re

# Объявление имён файлов для работы
source_file = input('Введите файл для проверки: ')
result_file = 'result.txt'

# Отрываем файл для записи
with open(result_file, 'w') as out_file:

    try:

        # Открываем файл для чтения
        with open(source_file) as in_file:

            # Задаём параметры поиска
            string_for_search = input('Введите строку для поиска: ')
            pattern = re.compile(re.escape(string_for_search))

            # Проходим по каждой строке файла
            for line in in_file:

                # Ищем совпадения
                result = pattern.search(line)

                # Если совпадение есть, то записываем строку в файл для записи
                if result is not None:
                    out_file.write(line)

    except FileNotFoundError:
        print('Указанный файл не найден')