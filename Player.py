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
   
    def takedamage(self, injury):
        self.hp = self.hp - injury
