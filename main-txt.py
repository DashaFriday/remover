import re

source_file = input('Введите файл для проверки: ')
result_file = 'result.txt'

with open(result_file, 'w') as out_file:

    try:
        with open(source_file) as in_file:

            string_for_search = input('Введите строку для поиска: ')
            pattern = re.compile(re.escape(string_for_search))

            for line in in_file:

                result = pattern.search(line)

                if result is not None:
                    out_file.write(line)

    except FileNotFoundError:
        print('Указанный файл не найден')
