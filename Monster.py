#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:01:46 2021

@author: arnavchokshi
"""
import random
class Monster:
    def __init__ ():
        hp = random.randint(50, 200)
        damage = random.randint(10, 50)
        toughness = random.randint(0, 20)
        pointvalue = hp + 4 * damage + 10 * toughness
    
    def intro():
        print("A monster has appeared!")
        
    def desc(self):
        print("HP: ", self.hp)
        print("Damage: ", self.damage)
        print("Toughness: ", self.toughness)
        print("Point value: ", self.pointvalue)
        
    def takedamage(self, injury):
        self.hp = self.hp - injury
    
        
