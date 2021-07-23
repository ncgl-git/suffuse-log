import unittest

from . import ansi_config


class TestAnsiConfig(unittest.TestCase):
    def test_style(self):

        input_ = "value with spaces and , | complex / characters "
        styles = ("red_fore", "blue_back")

        actual = ansi_config.AnsiConfig.style(input_, styles)
        expected = "\x1b[31m\x1b[44mvalue with spaces and , | complex / characters \x1b[0m"

        self.assertEqual(actual, expected)
