from random import randint


class Basic:
    def __init__(self, name):
        self.atName = name
        self.atHP = 100
        self.atMN = 50

    def status(self):
        print(f'Name: {self.atName}\n'
              f'HP: {self.atHP}\n'
              f'MN: {self.atMN}')

    def mana_poiton(self):
        self.atname = 'Mana Poiton'
        self.atMN += 20
        print(f'{self.atName} drink {self.atname}')

    def heal_poiton(self):
        self.atname = 'Heal Poiton'
        self.atHP += 35
        print(f'{self.atName} drink {self.atname}')


class Hero(Basic):
    def __init__(self, name):
        super().__init__(name)
        self.atSila = 10
        self.atInt = 5
        self.atLov = 5
        self.atExp = 0
        self.atLvl = 0

    def status(self):
        super().status()
        print(f'Sila:{self.atSila}\nInt:{self.atInt}\nLov:{self.atLov}\nExp:{self.atExp}\nLvl:{self.atLvl}\n')

    def scream(self):
        print(f'Я будущий герой {self.atName}, но я не выбрал специальность.')
        cmd = input('1 - воин, 2 - маг, 3 - лучник')
        if cmd == '1':
            print(f'Я {self.atName} стану великим воином! Теперь помоги мне определиться с оружием')
            cmd = input('1 - Меч, 2 - Топор, 3 - Кувалда')
            if cmd == '1':
                print('Острое лезвие моего меча пронзит врага!')

            elif cmd == '2':
                print('Да поможет мне сила топора!')

            elif cmd == '3':
                print('С этой кувалдой я непобедим!')

        elif cmd == '2':
            print(f'Я {self.atName} буду жить в памяти жителей Альгоры как несокрушимый маг! Теперь помоги мне определиться с оружием')
            cmd = input('1 - Скрипер-меч, 2 - Посох, 3 - книга с заклинаниями')
            if cmd == '1':
                print('С этим мечом я не дам в обиду жителей Альгоры!')
            elif cmd == '2':
                print('Ух, я чувствую всю мощь посоха! Как потомок Эйдоры я обязан справиться со всеми трудностями')
            elif cmd == '3':
                print('На вид книга страха совсем не внушает.. Но нам ведь это в пользу! Уничтожим врагов исподтишка')

        elif cmd == '3':
            print(f'Я {self.atName} стану великим лучником, как Леголас! Теперь помоги мне определиться с оружием')
            cmd = input('1 - Лук, 2 - Рогатка, 3 - Арбалет')
            if cmd == '1':
                print('Я предвижу победу и только победу!')
            elif cmd == '2':
                print('Рогатка выглядела бы совсем безобидно, если бы не ее иглы, которыми я буду поражать врагов!')
            elif cmd == '3':
                print('Берегитесь, Чурчхеллы, я вас уничтожу!!!')

    def attack(self, target):
        cmd = input('1 - атаковать, 2 - убежать')


class Voin(Hero):
    def __init__(self, name='Ричард'):
        super()._init_(name)
        self.atGuns = 'Guns: Меч'
    def status(self):
        super().status()
        print(f'{self.atGuns}')


class Mag(Hero):
    def __init__(self, name='Ричард'):
        super()._init_(name)
        self.atGuns = 'Guns: Посох'
    def status(self):
        super().status()
        print(f'{self.atGuns}\n')

class Archier(Hero):
    def __init__(self, name='Ричард'):
        super()._init_(name)
        self.atGuns = 'Guns: Лук'
    def status(self):
        super(Archier, self).status()
        print(f'{self.atGuns}')

class NPC(Basic):
    def __init__(self, name='Давид'):
        super()._init_(name)
        self.atLVL = 1
    def status(self):
        super().status()
        print(f'LVL: 1')

class Travnik(NPC):
    def __init__(self, name='Боб'):
        super()._init_(name)
        self.atNPC.atLVL += self.randint(1, 10)
    def status(self):
        super().status()
        print(f'{self.atLVL}')

class Gameplay:
    hero = Hero('Ричард')

    def __init__(self):
        from random import choice
        self.atStep = 1

        self.atKarta = [['_' for j in range(20)] for i in range(20)]

        self.atMC = "X"
        self.atMestoX = 10
        self.atMestoY = 5
        self.atKarta[self.atMestoY][self.atMestoX] = self.atMC

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

    def interface(self):
        print(f'Step:{self.atStep}')
        for s in self.atKarta: #Визуализация карты вместо print(*self.atKarta)
            print(*s)
        self.atMC.review()
        print(f'1 - walk, 2 - eat, ...')

    def walk(self):
        cmd = input('1 - left, 2 - right, 3 - up, 4 - down:')
        #горизонталь ось X
        if cmd == '2':
            self.atMC.walk()
            self.atKarta[self.atMestoY][self.atMestoX] = '_'
            self.atMestoX += 1
            self.atMC.eat(self.atKarta[self.atMestoY][self.atMestoX])
            self.atKarta[self.atMestoY][self.atMestoX] = self.atMC
        if cmd == '1':
            self.atMC.walk()
            self.atKarta[self.atMestoY][self.atMestoX] = '_'
            self.atMestoX -= 1
            self.atMC.eat(self.atKarta[self.atMestoY][self.atMestoX])
            self.atKarta[self.atMestoY][self.atMestoX] = self.atMC
        #вертикаль ось Y
        if cmd == '3':
            self.atMC.walk()
            self.atKarta[self.atMestoY][self.atMestoX] = '_'
            self.atMestoY -= 1
            self.atMC.eat(self.atKarta[self.atMestoY][self.atMestoX])
            self.atKarta[self.atMestoY][self.atMestoX] = self.atMC
        if cmd == '4':
            self.atMC.walk()
            self.atKarta[self.atMestoY][self.atMestoX] = '_'
            self.atMestoY += 1
            self.atMC.eat(self.atKarta[self.atMestoY][self.atMestoX])
            self.atKarta[self.atMestoY][self.atMestoX] = self.atMC

Gameplay()



