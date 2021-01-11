import unittest
from Monster import Monster
class TestHero(unittest.TestCase):
    def setUp(self):
        self.monster = Monster()
    def test_damage_true(self):
        self.assertEqual(self.monster.damage(),208)

    def test_damage_false(self):
        self.assertEqual(self.monster.damage(),196)

    def test_spell_true(self):
        self.assertEqual(self.monster.spell(),161)

    def test_spell_false(self):
        self.assertEqual(self.monster.spell(),342)

if __name__ == "__main__":
 unittest.main()
