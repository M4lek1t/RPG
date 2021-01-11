from Hero import Hero
from Monster import Monster
from Battle import Battle

battle = Battle()
hero = Hero()
monster = Monster()

print('----------------------------------')
print(hero.damage())
print(hero.spell())
print('----------------------------------')
print(monster.damage())
print(monster.spell())
print('----------------------------------')
print(battle.battle())


