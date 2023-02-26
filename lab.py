import random

class Base:
    def __init__(self, name, health, mana):
        self.atHP = health
        self.atMN = mana
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
            if self.atHP <= 0:
                self.enable = 0
            else:
                print(f'{self.name} получил урон {damage}, текущее здоровье {self.atHP}')
        else:
            print(f'{self.name} увернулся от атаки, текущее здоровье {self.atHP}')


    def setPos(self, X, Y):
        self.PosX = X
        self.PosY = Y

class BaseHero(Base):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)
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
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)
        self.atSila = 10
        self.atInt = 5
        self.atLov = 5
        self.atExp = 0
        self.atLvl = 0

        self.type = 0
        self.atGuns = None
        self.items = []

    def status(self):
        print(f'Sila:{self.atSila}\nInt:{self.atInt}\nLov:{self.atLov}\nExp:{self.atExp}\nLvl:{self.atLvl}\n')

    def scream(self):
        print(f'Я будущий герой {self.name}, но я не выбрал специальность.')
        cmd = input('1 - воин, 2 - маг, 3 - лучник, 4 - травник: ')
        if cmd == '1':
            self.type = 1
        elif cmd == '2':
            self.type = 2
        elif cmd == '3':
            self.type = 3
        elif cmd == '4':
            self.type = 4

    def attack(self, target, damage):
        if self.type == 0:
            print(f'Я будущий герой {self.name}, и  я без оружия, но я нанес {target.name} урон {damage} своими  руками')
        else:
            print(f'Я будущий герой {self.name}, c помощью {self.atGuns}, я нанес {target.name} урон {damage}')
        target.hit(damage)

        if target.atHP <= 0:
            print(f'{target.name} повержен, получено 10 очков опыта')
            self.AddExp(10)

    def AddExp(self, count):
        self.atExp += count
        if self.atExp == 100:
            self.atLvl += 1
            self.LVLUP()
            self.atExp -= 100

    def LvlUP(self):
        return


class Voin(Hero):
    def __init__(self, health, mana, name='Ричард'):
        super().__init__(name, health, mana)
        self.atGuns = 'Guns: Меч'
        self.damage = 20

    def status(self):
        self.scream()
        super().status()

    def LvlUP(self):
        self.atSila += 3
        self.atLov += 2
        self.atInt += 1

    def scream(self):
        print(f'Я герой {self.name} и я воин с {self.atGuns}')


class Mag(Hero):
    def __init__(self, health, mana, name='Ричард'):
        super().__init__(name, health, mana)
        self.atGuns = 'Guns: Посох'
        self.zaklinania = []

    def status(self):
        self.scream()
        super().status()

    def scream(self):
        print(f'Я маг герой {self.name} и я знаю {len(self.zaklinania)}  заклинаний')

    def LvlUP(self):
        self.atSila += 1
        self.atLov += 2
        self.atInt += 4

    def add_magic(self, magic):
        self.zaklinania.append(magic)

class Archier(Hero):
    def __init__(self, health, mana, name='Ричард'):
        super().__init__(name, health, mana)
        self.atGuns = 'Guns: Лук'
        self.damage = 6

    def status(self):
        self.scream()
        super(Archier, self).status()

    def scream(self):
        print(f'Я герой {self.name} и я лучник с {self.atGuns}')


class NPC(BaseHero):
    def __init__(self, health, mana, lvl, name='Давид'):
        super().__init__(name, health, mana)
        self.atLVL = lvl

    def status(self):
        super().status()
        print(f'LVL: 1')

    def scream(self):
        print(f'Я {self.name} обычный NPC!')


class Travnik(NPC):
    def __init__(self, health, mana, lvl, name='Боб'):
        super().__init__(health, mana, lvl, name)
        self.damage = 0
        self.items = []

    def status(self):
        super().status()
        print(f'{self.atLVL}')

    def scream(self):
        print(f'Я {self.name} обычный травник!” ')

    def job(self, target, heal_potion):
        #Некоректые задачи для job и make_potion
        return

    def make_potion(self, heal_potion, heal_power):
        heal_potion.power = heal_power
        self.items.append(heal_potion)

class Kuznic(NPC):
    def __init__(self, health, mana, lvl, name='Колька'):
        super().__init__(health, mana, lvl, name)
        self.damage = 4

    def status(self):
        super().status()
        print(f'{self.atLVL}')

    def scream(self):
        print(f'Я {self.name} обычный кузнец!” ')

    def make_item(self, target, item):
        target.items.appened(item)

class Torgovec(NPC):
    def __init__(self, health, mana, lvl, name='Анакендий'):
        super().__init__(health, mana, lvl, name)
        self.damage = 4

    def status(self):
        super().status()
        print(f'{self.atLVL}')

    def scream(self):
        print(f'Я {self.name} обычный торговец!” ')

    def make_item(self, target, item):
        target.items.appened(item)

class Volshebnik(NPC):
    def __init__(self, health, mana, lvl, name='Гоша'):
        super().__init__(health, mana, lvl, name)
        self.damage = 4

    def status(self):
        super().status()
        print(f'{self.atLVL}')

    def scream(self):
        print(f'Я {self.name} обычный странствующий волшебника!” ')

    def make_item(self, target, item):
        target.items.appened(item)

class Enemy(Base):
    def __init__(self, name, health, mana, lvl):
        super().__init__(name, health, mana)
        self.lvl = lvl
        self.items = [Item(5)]
        self.isBoss = 0

    def Attack(self, target):
        target.hit(self.damage);
        print(f'{self.name} аттаковал {target.name}, нанёс {self.damage}, осталось {target.atHP}')

class Zombie(Enemy):
    def __init__(self, name, health, mana, lvl):
        super().__init__(name, health, mana, lvl)
        self.lvl = lvl
        self.items = [Item(10)]

    def Attack(self, target):
        target.hit(target.atMN / 5)
        print(f'{self.name} аттаковал {target.name}, нанёс {self.damage}, осталось {target.atHP}')

class Item:
    def __init__(self, count, id=0, name='монета'):
        self.name = name
        self.count = count
        self.id = id

class Bess(Enemy):
    def __init__(self, name, health, mana, lvl):
        super().__init__(name, health, mana, lvl)
        self.damage = 20
        self.isBoss = 1
        self.items = [Item(100)]

    def Attack(self, target):
        target.hit(self.damage);
        print(f'{self.name} аттаковал {target.name}, нанёс {self.damage}, осталось {target.atHP}')
        if random.randint(0, 100) < 30:
            self.steal_mana(target)

    def steal_mana(self, target):
        target.atMN -= 5
        print(f'{self.name} съел ману у {target.name}, кол-во: {self.damage}, осталось: {target.atMN}')

class Gameplay:
    def EnemySpawn(self):

        count = random.Random.randint(random, 0, self.EnemyCount / 2)
        for i in range(count):
            enemy = Zombie('Зомби', 100, 50, 5)
            enemy.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))
            enemy.str = 'z'

            self.Enemy.append(enemy)

        for i in range(self.EnemyCount - count):
            enemy = Enemy('Пират', 100, 50, 5)
            enemy.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))
            enemy.str = 'O'

            self.Enemy.append(enemy)


        enemy = Bess("Босс", 200, 100, 40)
        enemy.setPos(
            random.Random.randint(random, 0, self.Width - 1),
            random.Random.randint(random, 0, self.Height - 1))
        enemy.str = '#'

        self.Enemy.append(enemy)
        self.EnemyCount += 1

    def BuffsSpawn(self):
        ManaCount = random.Random.randint(random, 0, self.BuffsCount / 2)

        for i in range(ManaCount):
            buff = Base(1, 0, "Health Buff")
            buff.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))

            buff.damage = 0
            buff.str = 'H'

            self.Buffs.append(buff)

        for i in range(self.BuffsCount - ManaCount):
            buff = Base(1, 0, "Mana Buff")
            buff.setPos(
                random.Random.randint(random, 0, self.Width - 1),
                random.Random.randint(random, 0, self.Height - 1))

            buff.damage = 0
            buff.str = 'M'

            self.Buffs.append(buff)

    def NPCSpawn(self):
        travnik = Travnik(100, 50, random.randint(10, 50))
        travnik.str = '😤'
        travnik.setPos(
            random.Random.randint(random, 0, self.Width - 1),
            random.Random.randint(random, 0, self.Height - 1))
        self.NPC.append(travnik)

        travnik = Kuznic(100, 50, random.randint(10, 50))
        travnik.str = '🔨'
        travnik.setPos(
            random.Random.randint(random, 0, self.Width - 1),
            random.Random.randint(random, 0, self.Height - 1))
        self.NPC.append(travnik)

        travnik = Torgovec(100, 50, random.randint(10, 50))
        travnik.str = '👳'
        travnik.setPos(
            random.Random.randint(random, 0, self.Width - 1),
            random.Random.randint(random, 0, self.Height - 1))
        self.NPC.append(travnik)

        travnik = Volshebnik(100, 50, random.randint(10, 50))
        travnik.str = '⭐'
        travnik.setPos(
            random.Random.randint(random, 0, self.Width - 1),
            random.Random.randint(random, 0, self.Height - 1))
        self.NPC.append(travnik)

    def __init__(self):
        self.Enemy = []
        self.Buffs = []
        self.NPC = []

        self.BuffsCount = 10
        self.Width = 40
        self.Height = 10
        self.EnemyCount = 30

        self.BuffsSpawn()
        self.EnemySpawn()
        self.NPCSpawn()

        self.atStep = 1

        self.atKarta = [['_' for j in range(self.Width)] for i in range(self.Height)]

        self.hero = Hero('Ричард', 100, 50)
        self.hero.setPos(3, 3)
        self.atKarta[self.hero.PosY][self.hero.PosX] = self.hero.str
        for i in range(self.EnemyCount):
            self.atKarta[self.Enemy[i].PosY][self.Enemy[i].PosX] = "O"

        print('Игра началась')
        self.start()

    def start(self):
        self.hero.scream()

        hero = self.hero
        if self.hero.type == 1:
            hero = Voin(200, 50, hero.name)
        elif self.hero.type == 2:
            hero = Mag(200, 50, hero.name)
        elif self.hero.type == 3:
            hero = Archier(200, 50, hero.name)

        hero.setPos(self.hero.PosX, self.hero.PosY)
        hero.type = self.hero.type
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
                    self.hero.attack(Enemy, self.hero.damage)

                    if Enemy.enable == 1:
                        self.hero.hit(Enemy.damage)
                        if self.hero.atHP <= 0:
                            print(f'Выс убили, и вы проиграли. Game over')
                            return
                    elif Enemy.isBoss == 1:
                        print(f'Поздравляю вы прошли игру, игра закончена')
                        return
                    else:
                        print(f'За убийтсво {Enemy.name} вы получили:')
                        for i in range(len(Enemy.items)):
                            print(f'{Enemy.items[i].name}: {Enemy.items[i].count}')

            elif cmd == 'break':
                print(f'Игра прервана')
                return
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
                self.atKarta[self.Enemy[i].PosY][self.Enemy[i].PosX] = self.Enemy[i].str

        for i in range(4):
            self.atKarta[self.NPC[i].PosY][self.NPC[i].PosX] = self.NPC[i].str

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