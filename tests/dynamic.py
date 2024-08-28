from lib.dynamic import dist
import unittest


class TestDist(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(dist("", ""), 0)

    def test_i_an(self):
        self.assertEqual(dist("i", "an"), 2)

    def test_kitten_sitting(self):
        self.assertEqual(dist("kitten", "sitting"), 3)

    def test_alpha_aleph(self):
        self.assertEqual(dist("alpha", "aleph"), 2)

    def test_longer(self):
        self.assertEqual(
            dist("a man, a plan, a canal: panama", "a girl, a pearl, a lexus: canada"),
            14,
        )


if __name__ == "__main__":
    unittest.main()
