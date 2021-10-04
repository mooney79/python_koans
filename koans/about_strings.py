#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    # https://docs.python.org/3/library/stdtypes.html#textseq
    # https://docs.python.org/3/library/unittest.html#assert-methods
    # https://docs.python.org/3/library/functions.html#isinstance


    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    # Both string and bytes literals may optionally be prefixed with a letter 'r' 
    # or 'R'; such strings are called raw strings and treat backslashes as literal 
    # characters. As a result, in string literals, '\U' and '\u' escapes in raw 
    # strings are not treated specially. Given that Python 2.x’s raw unicode 
    # literals behave differently than Python 3.x’s the 'ur' syntax is not supported.
    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual('He said, "Go Away."', string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual(r"Don't", string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))
# https://docs.python.org/3/library/functions.html#len
    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
