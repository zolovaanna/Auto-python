import pytest
from string_utils import StringUtils

class TestStringUtils:


    def setup_method(self):

        self.string_utils = StringUtils()

    def test_is_empty_empty_string(self):

        assert self.string_utils.is_empty("")

    def test_is_empty_non_empty_string(self):

        assert not self.string_utils.is_empty("Test")

    def test_is_whitespace_empty_string(self):

        assert self.string_utils.is_whitespace("")

    def test_is_whitespace_whitespace_string(self):

        assert self.string_utils.is_whitespace(" ")

    def test_is_whitespace_non_whitespace_string(self):

        assert not self.string_utils.is_whitespace("Test ")

    def test_is_numeric_numeric_string(self):

        assert self.string_utils.is_numeric("123")

    def test_is_numeric_float_string(self):

        assert self.string_utils.is_numeric("123.45")

    def test_is_numeric_non_numeric_string(self):

        assert not self.string_utils.is_numeric("Test")

    def test_reverse_empty_string(self):

        assert self.string_utils.reverse("") == ""

    def test_reverse_non_empty_string(self):

        assert self.string_utils.reverse("Test") == "tseT"

    def test_capitalize_words_empty_string(self):

        assert self.string_utils.capitalize_words("") == ""

    def test_capitalize_words_single_word(self):

        assert self.string_utils.capitalize_words("test") == "Test"

    def test_capitalize_words_multiple_words(self):

        assert self.string_utils.capitalize_words("test string") == "Test String"

    def test_count_words_empty_string(self):

        assert self.string_utils.count_words("") == 0

    def test_count_words_single_word(self):

        assert self.string_utils.count_words("Test") == 1

    def test_count_words_multiple_words(self):

        assert self.string_utils.count_words("Test string") == 2

    def test_replace_chars_empty_string(self):

        assert self.string_utils.replace_chars("", "a", "b") == ""

    def test_replace_chars_single_char(self):

        assert self.string_utils.replace_chars("Test", "T", "t") == "test"

    def test_replace_chars_multiple_chars(self):

        assert self.string_utils.replace_chars("Test", "t", "T") == "TesT"

    def test_trim_empty_string(self):

        assert self.string_utils.trim("") == ""

    def test_trim_whitespace_string(self):

        assert self.string_utils.trim(" Test ") == "Test"

    def test_trim_non_whitespace_string(self):

        assert self.string_utils.trim("Test") == "Test"
