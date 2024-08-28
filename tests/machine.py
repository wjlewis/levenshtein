import unittest
from lib.gen_insts import *
from lib.machine import run


class TestMachine(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(run("", []), "")

    def test_insert(self):
        self.assertEqual(run("", [Insert("a")]), "a")

    def test_delete(self):
        self.assertEqual(run("b", [Delete("b")]), "")

    def test_replace(self):
        self.assertEqual(run("z", [Replace("z", "y")]), "y")

    def test_skip(self):
        self.assertEqual(run("ab", [Skip(), Skip()]), "ab")

    def test_alpha_aleph(self):
        insts = gen_insts("alpha", "aleph")
        self.assertEqual(run("alpha", insts), "aleph")

    def test_kitten_sitting(self):
        insts = gen_insts("kitten", "sitting")
        self.assertEqual(run("kitten", insts), "sitting")


if __name__ == "__main__":
    unittest.main()
