#!/usr/bin/env python3

import unittest
from script import say_hello 

class TestScript(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(say_hello("MAKAR"), "Hello, MAKAR")

    def test_hello_2(self):
        self.assertEqual(say_hello("Vadim"), "Hello, Vadim")


if __name__ == "__main__":
    unittest.main()
