import random
class Player:
    def __init__(self, name : str, exp : int, level : int, nemeses : list) -> None:
        """create a new player object

        Args:
            name (str): player name
            exp (int): starting exp
            level (int): starting level
            nemeses (list): list of enemie
        """
        self.name = name
        self.hp = 100
        self.exp = exp
        self.level = level
        self.nemeses = nemeses

    def attack(self, enemy):
        """attack another player and adds the object into
            the other players enemy list

        Args:
            enemy (Player): given player to attack
        """
        if not enemy:
            enemy = self.nemeses[len(self.nemeses) - 1]
        enemy.hp -= random.randint(5, 20) * self.level
        if not (self in enemy.nemeses):
            enemy.nemeses.append(self)

    def revive(self):
        """restore the hp of the player to 100
        """
        self.hp = 100

