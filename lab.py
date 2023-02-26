import random

class Base:
    def __init__(self, name):
        self.atHP = 100
        self.atMN = 50
        self.name = name
        self.str = "X"

        self.PosX = 0
        self.PosY = 0

        self.damage = 5
        self.enable = 1 #1 - включено, 0 - выколючено (мертво)

        #Делаем систему миссов
        self.miss = 0.1

    def hit(self, damage):
        if damage == 0:
            return

        #Система миссов (уклонения)
        if random.randint(0, 100) > self.miss * 100:
            self.atHP -= damage
            print(f'{self.name} получил урон {damage}, текущее здоровье {self.atHP}')
        else:
            print(f'{self.name} увернулся от атаки, текущее здоровье {self.atHP}')

    def setPos(self, X, Y):
        self.PosX = X
        self.PosY = Y

class BaseHero(Base):
    def __init__(self, name):
        super().__init__(name)
        self.miss = 0.3

    def drink_heal_potion(self, potion):
        self.atHP += potion
        print(f'{self.name} drink Health Potion')

    def drink_mana_potion(self, potion_mana):
        self.atMN += potion_mana
        print(f'{self.name} drink Mana Potion')

    def tryEat(self, Eat):
        if Eat is None :
            return

        if Eat.enable == 0:
            return

        if Eat.str == 'M':
            self.drink_mana_potion(20)
        if Eat.str == 'H':
            self.drink_heal_potion(20)


class Hero(BaseHero):
    def __init__(self, name):
        super().__init__(name)
        self.atSila = 10
        self.atInt = 5
        self.atLov = 5
        self.atExp = 0
        self.atLvl = 0

        self.type = 0

    def status(self):
        print(f'Sila:{self.atSila}\nInt:{self.atInt}\nLov:{self.atLov}\nExp:{self.atExp}\nLvl:{self.atLvl}\n')

    def scream(self):
        print(f'Я будущий герой {self.name}, но я не выбрал специальность.')
        cmd = input('1 - воин, 2 - маг, 3 - лучник, 4 - травник: ')
        if cmd == 1:
            type = 1
        elif cmd == 2:
            type = 2
        elif cmd == 3:
            type = 3
        elif cmd == 4:
            type = 4

    def attack(self, target, damage):
        print(f'Я будущий герой{self.name}, и  я без оружия, но я нанес {target.name} урон {damage} своими  руками')
        target.hit(damage)
        if(target.atHP == 0):
            print(f'{target.name} повержен, получено 20 очков опыта')
            self.AddExp(20)

    def AddExp(self, count):
        self.atExp += count


class Voin(Hero):
    def __init__(self, name='Ричард'):
        super()._init_(name)
        self.atGuns = 'Guns: Меч'
        self.damage = 20

    def status(self):
        super().status()
        print(f'{self.atGuns}')


class Mag(Hero):
    def __init__(self, name='Ричард'):
        super()._init_(name)
        self.atGuns = 'Guns: Посох'
        self.damage = 8

    def status(self):
        super().status()
        print(f'{self.atGuns}\n')


class Archier(Hero):
    def __init__(self, name='Ричард'):
        super()._init_(name)
        self.atGuns = 'Guns: Лук'
        self.damage = 6

    def status(self):
        super(Archier, self).status()
        print(f'{self.atGuns}')


class NPC(BaseHero):
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
        self.damage = 4

    def status(self):
        super().status()
        print(f'{self.atLVL}')

class Gameplay:
    def EnemySpawn(self):
        for i in range(self.EnemyCount):
            enemy = Base("Монстр")
            enemy.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))

            self.Enemy.append(enemy)
    def BuffsSpawn(self):
        ManaCount = random.Random.randint(random, 0, self.BuffsCount / 2)

        for i in range(ManaCount):
            buff = Base("Health Buff")
            buff.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))

            buff.damage = 0
            buff.str = 'H'

            self.Buffs.append(buff)

        for i in range(self.BuffsCount - ManaCount):
            buff = Base("Mana Buff")
            buff.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))

            buff.damage = 0
            buff.str = 'M'

            self.Buffs.append(buff)

    def __init__(self):
        self.Enemy = []
        self.Buffs = []
        self.BuffsCount = 10
        self.Width = 40
        self.Height = 10
        self.EnemyCount = 10

        self.BuffsSpawn()
        self.EnemySpawn()

        self.atStep = 1

        self.atKarta = [['_' for j in range(self.Width)] for i in range(self.Height)]

        self.hero = Hero('Ричард')
        self.hero.setPos(3,3)
        self.atKarta[self.hero.PosY][self.hero.PosX] = self.hero.str
        for i in range(self.EnemyCount):
            self.atKarta[self.Enemy[i].PosY][self.Enemy[i].PosX] = "O"

        print('Игра началась')
        self.start()

    def start(self):
        self.hero.scream()

        hero = self.hero
        if(self.hero.type == 1):
            hero = Voin;
        elif (self.hero.type == 2):
            hero = Mag;
        elif (self.hero.type == 3):
            hero = Archier;
        elif (self.hero.type == 4):
            hero = Travnik;

        hero.setPos(self.hero.PosX, self.hero.PosY)
        self.hero = hero

        self.interface()

        while True:
            #Проверка врагов
            Enemy = None

            for i in range(self.EnemyCount):
                if(self.Enemy[i].PosX == self.hero.PosX):
                    if(self.Enemy[i].PosY == self.hero.PosY):
                        if(self.Enemy[i].enable == 1):
                            Enemy = self.Enemy[i]


            cmd = input('Action:')
            if cmd == '1':
                self.walk()
            elif cmd == '3':
                self.hero.status()
                continue
            elif cmd == '2':
                #Смотрим по бафам и ищем баф, с теми координатами, где стоит игрок
                Eat = None
                for i in range(self.BuffsCount):
                    if (self.Buffs[i].PosX == self.hero.PosX):
                        if (self.Buffs[i].PosY == self.hero.PosY):
                            if(self.Buffs[i].enable == 1):
                                Eat = self.Buffs[i]

                self.hero.tryEat(Eat)

                #Если тут был враг, то бьём игрока
                if Enemy != None:
                    self.hero.hit(Enemy.damage)
            elif cmd == '4':
                if Enemy is not None:
                    self.hero.attack(self.Enemy[i], self.hero.damage)
                    if(Enemy.atHP <= 0):
                        Enemy.enable = 0
                    #враг должен ударить
                    self.hero.hit(Enemy.damage)

            else:
                print("Нет такой команды")
            self.interface()
            self.atStep += 1

    def interface(self):
        for i in range(self.BuffsCount):
            if self.Buffs[i].enable == 1:
                self.atKarta[self.Buffs[i].PosY][self.Buffs[i].PosX] = self.Buffs[i].str

        for i in range(self.EnemyCount):
            if self.Enemy[i].enable == 1:
                self.atKarta[self.Enemy[i].PosY][self.Enemy[i].PosX] = 'O'

        self.atKarta[self.hero.PosY][self.hero.PosX] = 'X'

        print(f'Step:{self.atStep}')
        for s in self.atKarta:  # Визуализация карты вместо print(*self.atKarta)
            print(*s)
        print(f'1 - walk, 2 - eat, ...')

    def walk(self):
        cmd = input('1 - left, 2 - right, 3 - up, 4 - down:')
        # горизонталь ось X
        self.atKarta[self.hero.PosY][self.hero.PosX] = '_'

        if cmd == '2':
            self.hero.PosX += 1
        if cmd == '1':
            self.hero.PosX -= 1
        # вертикаль ось Y
        if cmd == '3':
            self.hero.PosY -= 1
        if cmd == '4':
            self.hero.PosY += 1

        self.atKarta[self.hero.PosY][self.hero.PosX] = self.hero.str

Gameplay()