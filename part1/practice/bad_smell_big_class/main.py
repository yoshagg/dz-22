# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

class Obj:
    ##
    # тут представлено поведение четырех различных игровых объектов:
    # - воина
    # - лекаря
    # - дерева
    # - ловушки
    def __init__(self, hp=0, damage=0, defense=0, speed=0):
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.speed = speed

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass


class Warrior(Obj):
    def __init__(self, hp=228, damage=228, defense=228, speed=228):
        super().__init__(hp, damage, defense, speed)

class Healer(Obj):
    def __init__(self, hp=10, defense=10, speed=62162162716271):
        super().__init__(hp, defense, speed)

    def heal(self):
        pass


class MotherFuckingTree(Obj):
    def __init__(self, hp=1000, defense=400):
        super().__init__(hp, defense)

    def on_fire(self):
        pass


class Trap(Obj):
    def __init__(self, damage=100):
        super().__init__(damage)


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
