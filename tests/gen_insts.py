from lib.gen_insts import *
import unittest


class TestInstGen(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(gen_insts("", ""), [])

    def test_insert(self):
        self.assertEqual(gen_insts("", "ab"), [Insert("a"), Insert("b")])

    def test_delete(self):
        self.assertEqual(gen_insts("ab", ""), [Delete("a"), Delete("b")])

    def test_replace(self):
        self.assertEqual(gen_insts("a", "b"), [Replace("a", "b")])

    def test_skip(self):
        self.assertEqual(gen_insts("abc", "abc"), [Skip(), Skip(), Skip()])

    def test_alpha_aleph(self):
        self.assertEqual(
            gen_insts("alpha", "aleph"),
            [Skip(), Skip(), Insert("e"), Skip(), Skip(), Delete("a")],
        )


if __name__ == "__main__":
    unittest.main()
