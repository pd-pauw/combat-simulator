from enum import Enum

class Action_orientation(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class Character:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor
        self.attack = 0
        self.defence = 0

        def defend(action_orientation: Action_orientation):
            pass
        def attack(action_orientation: Action_orientation):
            pass
        def use_consumable():
            pass

class PlayerCharacter(Character):
    pass

class EnemyCharacter(Character):
    pass

