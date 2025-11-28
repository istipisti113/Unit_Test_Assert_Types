# import module
import pytest
from text_processor import *
# from file import class


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    assert TextProcessor().capitalize_text("alma") == "ALMA"


def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    assert TextProcessor().capitalize_text("alma") != "alma"

def test_reverse_text_in():
    """3. Assert in - benne van"""
    assert TextProcessor.reverse_text("alma") == "amla"


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    assert TextProcessor.reverse_text("alma") != "alma"


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    asd = TextProcessor.count_words("indul a gorog aludni")
    assert asd == 4
    assert isinstance(asd, int)


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    assert TextProcessor.count_words("indul a gorog aludni") >3 is True


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    assert TextProcessor.count_words("") == 0


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    assert TextProcessor.is_palindrome("indul a gorog aludni") == True


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    assert TextProcessor.remove_spaces("a b c d") == "abcd" 