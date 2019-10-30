# @property装饰器
# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name
#
#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age
#
#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
#
# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     # person.name = '白元芳'  # AttributeError: can't set attribute
#
#
# if __name__ == '__main__':
#     main()

# -----------------------------------------------------------------------

# __slots__魔法:动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
#               但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
#               需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

# class Person(object):
#
#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
#
# def main():
#     person = Person('王大锤', 22)
#     person.play()
#     person._gender = '男'
#
#     # person._is_gay = True
#     # AttributeError: 'Person' object has no attribute '_is_gay'
#
# if __name__ == '__main__':
#     main()

# ------------------------------------------------------------------------

# 静态方法和类方法
# 之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
# 实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，
# 并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，
# 这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），
# 所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题

# from math import sqrt
#
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) *
#                     (half - self._b) * (half - self._c))
#
#
# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
#         # print(Triangle.perimeter(t))
#         print(t.area())
#         # print(Triangle.area(t))
#     else:
#         print('无法构成三角形.')
#
#
# if __name__ == '__main__':
#     main()


# 类方法
# 和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
# 它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
# 通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
# from time import time, localtime, sleep
#
#
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     # 通过类方法创建对象并获取系统时间
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()

# ---------------------------------------------------------------------------------------------

#类之间的关系:UML

# ----------------------------------------------------------------------------------------------

# 继承和多态
# 刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
# 从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
# 子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，
# 在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。
#
# class Person(object):
#     """人"""
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         print('%s正在愉快的玩耍.' % self._name)
#
#     def watch_av(self):
#         if self._age >= 18:
#             print('%s正在观看爱情动作片.' % self._name)
#         else:
#             print('%s只能观看《熊出没》.' % self._name)
#
#
# class Student(Person):
#     """学生"""
#
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade, self._name, course))
#
#
# class Teacher(Person):
#     """老师"""
#
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self, title):
#         self._title = title
#
#     def teach(self, course):
#         print('%s%s正在讲%s.' % (self._name, self._title, course))
#
#
# def main():
#     stu = Student('王大锤', 15, '初三')
#     stu.study('数学')
#     stu.watch_av()
#     t = Teacher('骆昊', 38, '砖家')
#     t.teach('Python程序设计')
#     t.watch_av()
#
#
# if __name__ == '__main__':
#     main()

# 多态
# 子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
# 通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
# 不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

# from abc import ABCMeta, abstractmethod
#
#
# class Pet(object, metaclass=ABCMeta):
#     """宠物"""
#
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         """发出声音"""
#         pass
#
#
# class Dog(Pet):
#     """狗"""
#
#     def make_voice(self):
#         print('%s: 汪汪汪...' % self._nickname)
#
#
# class Cat(Pet):
#     """猫"""
#
#     def make_voice(self):
#         print('%s: 喵...喵...' % self._nickname)
#
#
# def main():
#     pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
#     for pet in pets:
#         pet.make_voice()
#
#
# if __name__ == '__main__':
#     main()

# 在上面的代码中，我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
# Python从语法层面并没有像Java或C那样提供对抽象类的支持，但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到
# 抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，Dog和Cat两个子类分别对Pet类中的
# make_voice抽象方法进行了重写并给出了不同的实现版本，当我们在main函数中调用该方法时，这个方法就表现出了多态行为（
# 同样的方法做了不同的事情）。

# -------------------------------------------------------------------------------------------------

# 综合案例
# #
# from abc import ABCMeta, abstractmethod
# from random import randint, randrange
# from time import sleep
#
#
# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""
#
#     # 通过__slots__魔法限定对象可以绑定的成员变量
#     __slots__ = ('_name', '_hp')
#
#     def __init__(self, name, hp):
#         """初始化方法
#
#         :param name: 名字
#         :param hp: 生命值
#         """
#         self._name = name
#         self._hp = hp
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def hp(self):
#         return self._hp
#
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0
#
#     @property
#     def alive(self):
#         return self._hp > 0
#
#     @abstractmethod
#     def attack(self, other):
#         """攻击
#
#         :param other: 被攻击的对象
#         """
#         pass
#
#
# class Ultraman(Fighter):
#     """奥特曼"""
#
#     __slots__ = ('_name', '_hp', '_mp')
#
#     def __init__(self, name, hp, mp):
#         """初始化方法
#
#         :param name: 名字
#         :param hp: 生命值
#         :param mp: 魔法值
#         """
#         super().__init__(name, hp)
#         self._mp = mp
#
#     def attack(self, other):
#         other.hp -= randint(15, 25)
#
#     def huge_attack(self, other):
#         """究极必杀技(打掉对方至少50点或四分之三的血)
#
#         :param other: 被攻击的对象
#
#         :return: 使用成功返回True否则返回False
#         """
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False
#
#     def magic_attack(self, others):
#         """魔法攻击
#
#         :param others: 被攻击的群体
#
#         :return: 使用魔法成功返回True否则返回False
#         """
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False
#
#     def resume(self):
#         """恢复魔法值"""
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
#
#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp + \
#             '魔法值: %d\n' % self._mp
#
#
# class Monster(Fighter):
#     """小怪兽"""
#
#     __slots__ = ('_name', '_hp')
#
#     def attack(self, other):
#         other.hp -= randint(10, 20)
#
#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp
#
#
# def is_any_alive(monsters):
#     """判断有没有小怪兽是活着的"""
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False
#
#
# def select_alive_one(monsters):
#     """选中一只活着的小怪兽"""
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
#
#
# def display_info(ultraman, monsters):
#     """显示奥特曼和小怪兽的信息"""
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end='')
#
#
# def main():
#     u = Ultraman('骆昊', 1000, 120)
#     m1 = Monster('狄仁杰', 250)
#     m2 = Monster('白元芳', 500)
#     m3 = Monster('王大锤', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_alive(ms):
#
#         print('========第%02d回合========' % fight_round)
#         m = select_alive_one(ms)  # 选中一只小怪兽
#         skill = randint(1, 10)   # 通过随机数选择使用哪种技能
#         if skill <= 6:  # 60%的概率使用普通攻击
#             print('%s使用普通攻击打了%s.' % (u.name, m.name))
#             u.attack(m)
#             print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
#             if u.magic_attack(ms):
#                 print('%s使用了魔法攻击.' % u.name)
#             else:
#                 print('%s使用魔法失败.' % u.name)
#         else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
#             if u.huge_attack(m):
#                 print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
#             else:
#                 print('%s使用普通攻击打了%s.' % (u.name, m.name))
#                 print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
#             print('%s回击了%s.' % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
#         fight_round += 1
#         sleep(0.5)
#     print('\n========战斗结束!========\n')
#     if u.alive > 0:
#         print('%s奥特曼胜利!' % u.name)
#     else:
#         print('小怪兽胜利!')
#
#
# if __name__ == '__main__':
#     main()

# 扑克分发
#
# import random
#
#
# class Card(object):
#     """一张牌"""
#
#     def __init__(self, suite, face):
#         self._suite = suite
#         self._face = face
#
#     @property
#     def face(self):
#         return self._face
#
#     @property
#     def suite(self):
#         return self._suite
#
#     def __str__(self):
#         if self._face == 1:
#             face_str = 'A'
#         elif self._face == 11:
#             face_str = 'J'
#         elif self._face == 12:
#             face_str = 'Q'
#         elif self._face == 13:
#             face_str = 'K'
#         else:
#             face_str = str(self._face)
#         return '%s%s' % (self._suite, face_str)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Poker(object):
#     """一副牌"""
#
#     def __init__(self):
#         self._cards = [Card(suite, face)
#                        for suite in '♠♥♣♦'
#                        for face in range(1, 14)]
#         self._current = 0
#
#     @property
#     def cards(self):
#         return self._cards
#
#     def shuffle(self):
#         """洗牌(随机乱序)"""
#         self._current = 0
#         random.shuffle(self._cards)
#
#     @property
#     def next(self):
#         """发牌"""
#         card = self._cards[self._current]
#         self._current += 1
#         return card
#
#     @property
#     def has_next(self):
#         """还有没有牌"""
#         return self._current < len(self._cards)
#
#
# class Player(object):
#     """玩家"""
#
#     def __init__(self, name):
#         self._name = name
#         self._cards_on_hand = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def cards_on_hand(self):
#         return self._cards_on_hand
#
#     def get(self, card):
#         """摸牌"""
#         self._cards_on_hand.append(card)
#
#     def arrange(self, card_key):
#         """玩家整理手上的牌"""
#         self._cards_on_hand.sort(key=card_key)
#
#
# # 排序规则-先根据花色再根据点数排序
# def get_key(card):
#     return (card.suite, card.face)
#
#
# def main():
#     p = Poker()
#     p.shuffle()
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#     for _ in range(13):
#         for player in players:
#             player.get(p.next)
#     for player in players:
#         print(player.name + ':', end=' ')
#         player.arrange(get_key)
#         print(player.cards_on_hand)
#
#
# if __name__ == '__main__':
#     main()

# 工资系统

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()