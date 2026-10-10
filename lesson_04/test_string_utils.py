# test_string_utils.py
from string_utils import StringUtils

utils = StringUtils()

# --- capitalize ---

def test_capitalize_positive_normal():
    # позитивный: обычная строка
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_positive_already_capitalized():
    # позитивный: первая буква уже заглавная
    assert utils.capitalize("Skypro") == "Skypro"

def test_capitalize_negative_empty():
    # негативный: пустая строка
    assert utils.capitalize("") == ""

def test_capitalize_negative_only_spaces():
    # негативный: строка только из пробелов
    assert utils.capitalize("   ") == "   "


# --- trim ---

def test_trim_positive_leading_spaces():
    # позитивный: пробелы в начале
    assert utils.trim("   skypro") == "skypro"

def test_trim_negative_no_leading_spaces():
    # негативный: пробелов в начале нет
    assert utils.trim("skypro") == "skypro"

def test_trim_negative_empty_string():
    # негативный: пустая строка
    assert utils.trim("") == ""

def test_trim_negative_only_spaces_all_removed():
    # негативный: вся строка — пробелы, после удаления должно быть ""
    assert utils.trim("   ") == ""


# --- contains ---

def test_contains_positive_symbol_present():
    # позитивный: символ есть
    assert utils.contains("SkyPro", "S") is True

def test_contains_negative_symbol_absent():
    # негативный: символа нет
    assert utils.contains("SkyPro", "U") is False

def test_contains_negative_case_sensitive():
    # негативный: регистр не совпадает
    assert utils.contains("SkyPro", "s") is False

def test_contains_positive_substring():
    # позитивный: ищем подстроку (метод это поддерживает)
    assert utils.contains("SkyPro", "Pro") is True

def test_contains_negative_empty_symbol():
    # особый кейс: пустой символ. str.index("") всегда 0, поэтому вернёт True
    # это может быть дефектом (см. defects.txt)
    assert utils.contains("SkyPro", "") is True


# --- delete_symbol ---

def test_delete_symbol_positive_single_occurrence():
    # позитивный: один символ
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_positive_multiple_occurrences():
    # позитивный: несколько одинаковых символов
    assert utils.delete_symbol("banana", "a") == "bnn"

def test_delete_symbol_positive_substring():
    # позитивный: удаляем подстроку
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_negative_not_found():
    # негативный: символ/подстрока не найдена
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"

def test_delete_symbol_negative_empty_string():
    # негативный: входная строка пустая
    assert utils.delete_symbol("", "a") == ""

def test_delete_symbol_negative_remove_all():
    # негативный/крайний: удаляем всё
    assert utils.delete_symbol("aaaa", "a") == ""
