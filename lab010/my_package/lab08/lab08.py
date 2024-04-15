
from ctypes.wintypes import HPALETTE


def create_hero():
    max_hp = 100
    hp = max_hp
def Lab08_logic():
    # Тут можно разместить код логики
    is_dead = False

    def get_hp():
        return hp

    def change_hp(delta):
        nonlocal hp, is_dead
        
        if is_dead:
            return
        
        new_hp = hp + delta
        
        if new_hp > max_hp:
            hp = max_hp
        elif new_hp <= 0:
            hp = 0
            is_dead = True
        else:
            hp = new_hp

    def heal(amount):
        nonlocal hp, is_dead
        if is_dead:
            return
        change_hp(amount)

    def take_damage(amount):
        nonlocal hp, is_dead
        if is_dead:
            return
        change_hp(-amount)

    def resurrect():
        nonlocal hp, is_dead
        if not is_dead:
            return
        hp = 1
        is_dead = False

    return get_hp, heal, take_damage, resurrect

# Создаем экземпляр героя
hero_hp, hero_heal, hero_damage, hero_resurrect = create_hero()

# Пример использования
print(hero_hp())  # Выведет 100

hero_heal(50)  # Герой лечится на 50 HP
print(hero_hp())  # Выведет 100

hero_damage(75)  # Герой получает урон на 75 HP
print(hero_hp())  # Выведет 25

hero_damage(50)  # Герой получает урон на 50 HP
print(hero_hp())  # Выведет 0

hero_resurrect()  # Герой воскрешается
print(hero_hp())  # Выведет 1

hero_heal(50)  # Герой лечится на 50 HP
print(hero_hp())  # Выведет 51