from Hero import Hero

class Monster(Hero):
    def __init__(self, name='booba', lvl=99, hp=100):
        super().__init__(name, lvl, hp)
        self.rage = 65
        self.soul_pool = 23
        #print("ОБЭМЭ! ПОЧЕМУ ТАК НА***!?")

    def damage(self):
        if self.strength >= 1:
            self.punch = self.lvl + self.strength + self.rage
            print('Супер сильный удар!!!')
            return self.punch

    def spell(self):
        if self.intelligence >= 1:
            self.cast = self.lvl + self.intelligence + self.soul_pool
            print('Души мертвых внесут свой урон!!!')
            return self.cast


