rom StringUtils import StringUtils

string_utils = StringUtils()

# Тестирование метода capitalize
def test_capitilize():
    # Позитивные тесты
    assert string_utils.capitilize('skypro') == 'Skypro'  # Простой случай
    assert string_utils.capitilize('  skypro'.strip()) == 'Skypro'  # Пробелы в начале
    assert string_utils.capitilize('skypro  '.strip()) == 'Skypro'  # Пробелы в конце

    # Негативные тесты
    assert string_utils.capitilize('') == ''  # Пустая строка
    assert string_utils.capitilize(' ') == ' '  # Строка с пробелом

# Тестирование метода trim
def test_trim():
    # Позитивные тесты
    assert string_utils.trim('   skypro') == 'skypro'  # Пробелы в начале
    assert string_utils.trim('skypro') == 'skypro'  # Без пробелов

    # Негативные тесты
    assert string_utils.trim('') == ''  # Пустая строка
    assert string_utils.trim('  ') == ''  # Только пробелы

# Тестирование метода to_list
def test_to_list():
    # Позитивные тесты
    assert string_utils.to_list('a,b,c') == ['a', 'b', 'c']  # Простой случай
    assert string_utils.to_list('1:2:3', ':') == ['1', '2', '3']  # Другой разделитель

    # Негативные тесты
    assert string_utils.to_list('a,,b,c') == ['a', '', 'b', 'c']  # Пустые элементы
    assert string_utils.to_list('') == []  # Пустая строка
    assert string_utils.to_list('a,b,c,') == ['a', 'b', 'c', '']  # Запятая в конце

# Тестирование метода contains
def test_contains():
    # Позитивные тесты
    assert string_utils.contains('SkyPro', 'S') is True  # Символ найден
    assert string_utils.contains('abc', 'abc') is True  # Полное совпадение

    # Негативные тесты
    assert string_utils.contains('SkyPro', 'U') is False  # Символ не найден
    assert string_utils.contains('', 'a') is False  # Пустая строка
    assert string_utils.contains('abc', '') is True  # Пустая подстрока

# Тестирование метода delete_symbol
def test_delete_symbol():
    # Позитивные тесты
    assert string_utils.delete_symbol('SkyPro', 'k') == 'SyPro'  # Удаление символа
    assert string_utils.delete_symbol('abc123', '123') == 'abc'  # Удаление нескольких символов

    # Негативные тесты
    assert string_utils.delete_symbol('', 'a') == ''  # Пустая строка
    assert string_utils.delete_symbol('SkyPro', 'X') == 'SkyPro'  # Символ не найден

# Тестирование метода starts_with
def test_starts_with():
    # Позитивные тесты
    assert string_utils.starts_with('SkyPro', 'S') is True  # Символ в начале
    assert string_utils.starts_with('abc', 'a') is True  # Символ в начале

    # Негативные тесты
    assert string_utils.starts_with('SkyPro', 'U') is False  # Символ не найден
    assert string_utils.starts_with('', 'a') is False  # Пустая строка
    assert string_utils.starts_with('abc', 'X') is False  # Символ не найден

# Тестирование метода end_with
def test_end_with():
    # Позитивные тесты
    assert string_utils.end_with('SkyPro', 'o') is True  # Окончание совпадает
    assert string_utils.end_with('abc', 'c') is True  # Окончание совпадает

    # Негативные тесты
    assert string_utils.end_with('SkyPro', 'U') is False  # Окончание не совпадает
    assert string_utils.end_with('', 'a') is False  # Пустая строка
    assert string_utils.end_with('abc', 'X') is False  # Окончание не совпадает

# Тестирование метода list_to_string
def test_list_to_string():
    # Позитивные тесты
    assert string_utils.list_to_string(['a', 'b', 'c'], ',') == 'a,b,c'  # Простой случай
    assert string_utils.list_to_string(['a', 'b', 'c'], ':') == 'a:b:c'  # Другой разделитель

    # Негативные тесты
    assert string_utils.list_to_string(['a', '', 'b', 'c'], ',') == 'a,,b,c'  # Пустые элементы
    assert string_utils.list_to_string([]) == ''  # Пустой список
    assert string_utils.list_to_string(['a', 'b', 'c'], '') == 'abc'  # Без разделителя