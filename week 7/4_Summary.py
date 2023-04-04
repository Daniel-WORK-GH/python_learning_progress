import random

class Rectangle:
    def __init__(self, tl = (0, 0), br = (0, 0)) -> None:
        self.tl, self.br = tl, br
        self.width = abs(self.tl[0] - self.br[0])
        self.height = abs(self.tl[1] - self.br[1])

    def get_surface(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def randomize_start_point(self):
        self.tl = (
            random.randint(1, 100),
            random.randint(1, 100)
        )
    
    def randomize_end_point(self):
        self.br = (
            random.randint(1, 100),
            random.randint(1, 100)
        )
        

class Square:
    def __init__(self, side) -> None:
        self.side = side
    
    def get_surface(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return 2 * self.side + 2 * self.side
    
class Cube:
    def __init__(self, base_side, color) -> None:
        self.base = Square(base_side)
        self.side = base_side
        self.color = color

    def get_volume(self):
        return self.side ** 3
    
    def get_surface(self):
        return self.base.get_perimeter()
    
    def __str__(self) -> str:
        return f"Cube: base-{self.side}x{self.side} color:{self.color}"
    
class CubeTower:
    COLORS = ["black", "white"]

    def __init__(self) -> None:
        self.list : list[Cube] = []
        self.last : Cube = None

    def add_cube(self, cube : Cube): 
        if (not self.last or 
            (self.last.get_surface() > cube.get_surface() and self.last.color != cube.color)):
            self.list.append(cube)
            self.last = cube
            
    def randomize_tower(self):
        N = random.randint(0, 100)
        for _ in range(0, N):
            self.add_cube(
                Cube(random.randint(1, 100), random.choice(self.COLORS))
            )
    
    def __str__(self) -> str:
        strr = ""
        for i, x in enumerate(self.list):
            strr += f"{i} : {x}\n"
        return strr

ct = CubeTower()
ct.randomize_tower()
print(ct)