import random as rnd
from Hero import Hero
from Monster import Monster

hero = Hero()
monster = Monster()

hero.damage()
hero.spell()
monster.damage()
monster.spell()

class Battle:

    def __init__(self):
        self.chest = rnd.randint(1, 6)
        self.mon_hp = monster.hp
        self.hero_hp = hero.hp
        self.mon_punch = monster.punch
        self.hero_punch = hero.punch
        self.hero_cast = hero.cast
        self.mon_cast = monster.cast

    def battle(self):
        while self.hero_hp > 1:
            while self.mon_hp > 1:
                self.mon_hp -= (self.hero_punch + self.hero_cast)
                self.hero_hp -= (self.mon_punch + self.mon_cast)
            else:
                if self.hero_hp > 0 and self.mon_hp <= 0:
                    if self.chest == 1:
                        return 'Ты победил! В награду получаешь шмот уровня: POOP'
                    else:
                        if self.chest == 2:
                            return 'Ты победил! В награду получаешь шмот уровня: COMMON'
                        else:
                            if self.chest == 3:
                                return 'Ты победил! В награду получаешь шмот уровня: UNCOMMON '
                            else:
                                if self.chest == 4:
                                    return 'Ты победил! В награду получаешь шмот уровня: RARE'
                                else:
                                    if self.chest == 5:
                                        return 'Ты победил! В награду получаешь шмот уровня: LEGENDARY'
                                    else:
                                        if self.chest == 6:
                                            return 'Ты победил! В награду получаешь шмот уровня: IMMORTAL'
                else:
                    return 'Не смог смириться с поражением! И к чему это привело'