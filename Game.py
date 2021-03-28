from Monster import Monster
from Player import Player
import random

m_hp = random.randint(50, 200)
m_damage = random.randint(10, 50)
m_toughness = random.randint(0, 20)
m_pointvalue = m_hp + 4 * m_damage + 10 * m_toughness

p_hp = 100
p_damage = 25
p_armor = 0
p_rounds = 0
p_points = 0

monst = Monster(m_hp, m_damage, m_toughness, m_pointvalue)
player1 = Player(p_hp, p_damage, p_armor, p_rounds, p_points)
monst.intro()
player1.desc()
