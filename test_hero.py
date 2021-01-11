import unittest
from Hero import Hero
class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero()
    def test_damage_true(self):
        self.assertEqual(self.hero.damage(), 54)

    def test_damage_false(self):
        self.assertEqual(self.hero.damage(), 48)

    def test_workout_true(self):
        self.assertEqual(self.hero.workout(), 70)

    def test_workout_false(self):
        self.assertEqual(self.hero.workout(), 50)

    def test_spell_true(self):
        self.assertEqual(self.hero.spell(), 50)

    def test_spell_false(self):
        self.assertEqual(self.hero.spell(), 64)

    def test_scholl_true(self):
        self.assertEqual(self.hero.school(), 70)

    def test_school_false(self):
        self.assertEqual(self.hero.school(), 564)

    def test_sleep_true(self):
        self.assertEqual(self.hero.sleep(), 170)

    def test_sleep_false(self):
        self.assertEqual(self.hero.sleep(), 135)

if __name__ == "__main__":
 unittest.main()

