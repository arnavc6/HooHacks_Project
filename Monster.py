#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:01:46 2021

@author: arnavchokshi
"""
import random
class Monster:
    def __init__ (self, hp, damage, toughness, pointvalue):
        self.hp = hp
        self.damage = damage
        self.toughness = toughness
        self.pointvalue = pointvalue

    def intro(self):
        print("A monster has appeared!")
        
    def desc(self):
        print("HP: ", self.hp)
        print("Damage: ", self.damage)
        print("Toughness: ", self.toughness)
        print("Point value: ", self.pointvalue)
        
    def takedamage(self, injury):
        self.hp = self.hp - injury
