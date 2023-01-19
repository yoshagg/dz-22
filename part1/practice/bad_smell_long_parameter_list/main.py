# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, position: list, speed=1):
        self.position = position
        self.speed = speed

    def get_unit_position(self):
        return self.position

    def set_unit_position(self, sets: list):
        if len(sets) >= 2:
            self.position = sets
        else:
            raise "Задано слишком много аргументов. Нужно задать x и y координаты"

    def move(self, sets, direction):
        if direction == 'UP':
            up_sets = [sets[0], sets[1] + self.speed]
            self.set_unit_position(sets=up_sets)
        elif direction == 'DOWN':
            down_sets = [sets[0], sets[1] - self.speed]
            self.set_unit_position(sets=down_sets)
        elif direction == 'LEFT':
            left_sets = [sets[0] - self.speed, sets[1]]
            self.set_unit_position(sets=left_sets)
        elif direction == 'RIGTH':
            right_sets = [sets[0] + self.speed, sets[1]]
            self.set_unit_position(sets=right_sets)


class FlyingUnit(Unit):
    def __init__(self, position):
        self.position = position
        self.speed = 1.2


class CrawlingUnit(Unit):
    def __init__(self, position):
        self.position = position
        self.speed = 0.5


if __name__ == "__main__":
    u1 = Unit(position=[34294295, 3287472])
    fu1 = FlyingUnit(position=[34294295, 3287472])
    cu2 = CrawlingUnit(position=[34294295, 3287472])

    u1.move(sets=[3923929329, 9329392932], direction="UP")
    print(u1.get_unit_position())
