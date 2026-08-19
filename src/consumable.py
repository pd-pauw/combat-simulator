from character import Character
class Consumable:
    def __init__(self, name):
        self.name = name

    def consume():
        pass

class HealingPotion(Consumable):
    def __init__(self, name, heal_value):
        self.heal_value = heal_value 
        super().__init__(name)

    def consume(self, character: Character):
        character.health += self.heal_value