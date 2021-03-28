from Monster import Monster
from Player import Player
import random

p_hp = 100
p_damage = 25
p_armor = 0
p_rounds = 0
p_points = 0

m_hp = random.randint(50, 200)
m_damage = random.randint(10, 50)
m_toughness = random.randint(0, 20)
m_pointvalue = m_hp + 4 * m_damage + 10 * m_toughness

monst = Monster(m_hp, m_damage, m_toughness, m_pointvalue)
player1 = Player(p_hp, p_damage, p_armor, p_rounds, p_points)

guard = False
evade = False

def controlgame():
    print("Press 1 to start game, 0 to quit")
    game_state = int(input())
    if game_state == 1:
        monst.intro()
        print("Your stats: ")
        player1.desc()
        print("Monster's stats")
        monst.desc()
    while game_state != 0 and monst.hp != 0 and player1.hp != 0:
        playerattack()
        if m_hp <= 1:
            print("Monster killed!")
            player1.pointchange(p_rounds * m_pointvalue)
            player1.upgrade()
        monsterattack()
        if p_hp <= 0:
            print("Game over!")
            break


def playerattack():
    global guard
    global evade
    playerturn = player1.turn()
    if playerturn == 1:
        monst.takedamage(p_damage)
    elif playerturn == 2:
        guard = True
    elif playerturn == 3:
        evade = True


def monsterattack():
    global guard
    global evade
    if evade == True:
        dodge = random.randint(0, 1)
        if dodge != 1:
            print("Dodge failed!")
            player1.takedamage(m_damage)
            print(m_damage, " damage taken.")
        elif dodge == 1:
            print("Dodge successful!")
        evade = False
    elif guard == True:
        player1.takedamage(m_damage / 2)
        print(m_damage / 2, " damage taken.")
    else:
        player1.takedamage(m_damage)
        print(m_damage, " damage taken.")


controlgame()
