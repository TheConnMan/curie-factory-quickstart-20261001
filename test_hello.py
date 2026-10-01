"""Tests for the hello module."""

import unittest

import hello


class TestHello(unittest.TestCase):
    def test_hello_returns_hello(self):
        self.assertEqual(hello.hello(), "hello")


if __name__ == "__main__":
    unittest.main()
