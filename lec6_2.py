#Повторение классов

#pr1 Появление врагов на карте
import os


class Food:
    def __init__(self, n='_', en=0):
        self.atEN = en
        self.atN = n

    def __repr__(self):
        return f'{self.atN}'


class Persona:
    def __init__(self, name):
        self.atName = name
        self.atEnergy = 50
        self.atHP = 100

    def walk(self):
        print(f'{self.atName} is walking!')
        self.atEnergy -= 10

    def review(self):
        print(f'Name:{self.atName}  HP:{self.atHP}  Energy:{self.atEnergy}')

    def eat(self, thing):
        if isinstance(thing, Food):
            print(f'{self.atName} eat {thing.atN}')
            self.atEnergy += thing.atEN

    def fight(self, vrag):
        if isinstance(vrag, Enemy):
            print('***')
            print("ENEMY!!!!!!")
            print('***')
            while vrag.atHP > 0:
                cmd = input('1 - attack, 2 - run:')
                if cmd == '1':
                    print(f'{self.atName} attack {vrag.atName}')
                    vrag.atHP -= 10
                elif cmd == '2':
                    print(f'{self.atName} is coward!')
                vrag.attack(self)
                self.review()
                print(f'ENEMY:{vrag.atName}    HP:{vrag.atHP}')

    def __repr__(self):
        return self.atName[0]


class Enemy:
    def __init__(self):
        self.atName = 'skelet'
        self.atHP = 100

    def __repr__(self):
        return self.atName[0]

    def attack(self, hero):
        print(f'{self.atName} attack!')
        hero.atHP -= 20

class Gameplay:
    def __init__(self): #__init__ вызывается когда создается объект
        from random import choice
        self.atStep = 1
        self.atKarta = [choice(['_', '_', '_', '_', Food('*', 20), Food('**', 50), Enemy()]) for j in range(50)]

        self.atMC = Persona('Danil') #объект класса Persona
        self.atMesto = 3 #местоположение героя
        self.atKarta[self.atMesto] = self.atMC #cтавим героя на карту

        print('Игра началась')
        self.start()

    def start(self):


        while True:
            self.interface()
            cmd = input('Action:')
            if cmd == '1':
                self.walk()
            elif cmd == '2':
                print("Действия 2")
            else:
                print("Нет такой команды")
            self.atStep += 1
            os.system("CLS")

    def interface(self):
        print(f'Step:{self.atStep}')
        print(*self.atKarta)
        self.atMC.review()
        print(f'1 - walk, 2 - eat, ...')

    def walk(self):
        cmd = input('1 - left, 2 - right:')
        if cmd == '2':
            self.atMC.walk()
            self.atKarta[self.atMesto] = '_'
            self.atMesto += 1

            self.atMC.fight(self.atKarta[self.atMesto])
            self.atMC.eat(self.atKarta[self.atMesto])

            self.atKarta[self.atMesto] = self.atMC

        if cmd == '1':
            self.atMC.walk()
            self.atKarta[self.atMesto] = '_'
            self.atMesto -= 1

            self.atMC.fight(self.atKarta[self.atMesto])
            self.atMC.eat(self.atKarta[self.atMesto])

            self.atKarta[self.atMesto] = self.atMC



Gameplay()
'''
Задание: Дополняем пример!
1) Сделайте так, чтобы игра завершалась если HP героя была равна 0 или меньше.
2) Сделайте так, чтобы сила атаки героя зависила от энергии героя!
'''