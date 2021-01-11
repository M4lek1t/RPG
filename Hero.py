import math
class Hero:

    def __init__(self, name='Pepe', lvl=20, hp=1000):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = 44
        self.intelligence = 39
        self.energy = 100
        self.punch = 0
        self.cast = 0
        #print("БОЖЕ! КАКОЙ ЖЕ Я АХ**ННЫЙ!")

    def damage(self):
        if self.strength >= 50:
            self.punch = self.lvl + self.strength
            print('Это урон с удара:')
            return self.punch
        else:
            self.punch = self.lvl + math.ceil(self.strength/1.3)
            print('Это урон с удара с дебаффом:')
            self.workout()
            return self.punch


    def workout(self):
        while self.strength < 50 and self.energy > 0:
            self.strength += 10
            self.energy -= 10
        else:
            if self.energy <= 0:
                    print('Я устал!')
                    self.sleep()
            return self.energy


    def spell(self):
        if self.intelligence >= 50:
            self.cast = self.lvl + self.intelligence
            print('Это урон с заклинания:')
            return self.cast
        else:
            self.cast = self.lvl + math.ceil(self.intelligence/1.3)
            print('Это урон с заклинания с дебаффом:')
            self.school()
            return self.cast


    def school(self):
        while self.intelligence < 50 and self.energy > 0:
            self.intelligence += 10
            self.energy -= 10
        else:
            if self.energy <= 0:
                print('Мозг болит!!')
                self.sleep()
        return self.intelligence, self.energy

    def sleep(self):
        self.energy += 100
        if self.energy >= 100:
            self.damage()
            self.spell()
            return self.energy





