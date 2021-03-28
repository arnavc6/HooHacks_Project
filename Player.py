#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:20:47 2021
@author: arnavchokshi, mtran4
"""
import random
class Player:
    def __init__(self, hp, damage, armor, rounds, points):
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.rounds = rounds
        self.points = points

    def desc(self):
        print("HP: ", self.hp)
        print("Damage: ", self.damage)
        print("Armor: ", self.armor)
        print("Round number: ", self.rounds)
        print("Point value: ", self.points)

    def turn(self):
        turnNum = input("Choose an option (enter an int corresponding to your option of choice):\n1. Attack: deal damage to the monster\n2. Guard: take half damage from the monster's next attack\n3. Evade: attempt to dodge the monster's next attack (may fail)")
        if turnNum == 1:
            print("Monster took ", self.damage, " damage.")
        elif turnNum == 2:
            print("Guard stance active.")
        elif turnNum == 3:
            print("Ready to evade.")
        return turnNum

    def takedamage(self, injury):
        self.hp = self.hp - injury

    def upgrade(self):
        upgradeNum = input("Choose an option (enter an int corresponding to your option of choice):\n1. Heal: restore your HP to 100\n2. Weapon upgrade: increase damage by 5\n3. Armor upgrade: increase armor by 5")
        if(upgradeNum == 1):
            self.hp = 100
            print("HP restored to 100.")
        elif(upgradeNum == 2):
            self.damage = self.damage + 5
            print("Damage increased by 5.")
        elif(upgradeNum == 3):
            self.armor = self.armor + 5
            print("Armor increased by 5.")

    def pointchange(self, pointgain):
        self.points = self.points + pointgain
        print(pointgain, " points added to total")