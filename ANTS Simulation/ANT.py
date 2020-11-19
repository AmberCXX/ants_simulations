# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:10:18 2020

@author: amber
"""

class ANT:
    # property
    def __init__(self):
        self.lifeexpectation = 10
    
    # methods
    def printname(self):
        print('queen')
  
  
class QUEEN(ANT):
    # 只蚁后每秒钟能生出600只小蚂蚁
    # property
    def __init__(self):
        self.lifeexpectation = 10
        self.canreproduce = True
    
    # methods
    def printname(self):
        print('queen')
        
class FEMALE(QUEEN):
    # property
    def __init__(self):
        self.lifeexpectation = 10
        self.canreproduce = False
    
    # methods
    def ismature(self):
        self.canreproduce = True

class MALE(ANT):
    # property
    def __init__(self):
        self.lifeexpectation = 1
    
    # methods
    def printname(self):
        print('male')
        
class WORKER(ANT):
    #一般为群体中最小的个体，但数量最多。复眼小，单眼极微小或无。上颚、触角和三对足都很发达，善于步行奔走。
    #工蚁的主要职责是建造和扩大巢穴、采集食物、饲喂幼虫及蚁后等。
    # property
    def __init__(self):
        self.lifeexpectation = 1
    
    # methods
    def printname(self):
        print('worker')

class SOLDIER(ANT):
    #头大，上颚发达，可以粉碎坚硬食物，在保卫群体时即成为战斗的武器。
    # property
    def __init__(self):
        self.lifeexpectation = 1
    
    # methods
    def printname(self):
        print('male')