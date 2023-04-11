# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.

class Dragon:
    def __init__(self, height,fire,color) -> None:
        self.height = height
        self.fire = fire
        self.color = color

 

    def __lt__(self, other):
        return self.height < other.height and self.fire < other.fire and self.color < other.color
 
    def __le__(self, other):
        return self.height <= other.height and self.fire <= other.fire and self.color <= other.color
 
    def __gt__(self, other):
        return self.height > other.height and self.fire > other.fire and self.color > other.color
 
    def __ge__(self, other):
        return self.height >= other.height and self.fire >= other.fire and self.color >= other.color
 
    def __eq__(self, other):
        return self.height == other.height and self.fire == other.fire and self.color == other.color
 
    def __ne__(self, other):
        return self.height != other.height or self.fire != other.fire or self.color != other.color

    def __add__(self, other):
        self.height = int((self.height + other.height)/2)
        self.color = min(self.color, other.color)
        self.fire = max(self.fire, other.fire)
        
    def change_color(self, new_color):
        self.color = new_color

    def output(self, arg):
        print(self.fire * arg)

    def __sub__(self, other):
        self.height -= self.height//other
        self.fire += self.fire%other
        return self

    def __str__(self) -> str:
        return f"Dragon with height {self.height}, fire {self.fire} and color {self.color}"

    def __repr__(self) -> str:
        return f"Dragon({self.height}, {self.fire}, {self.color})"


dr1 = Dragon(69, 5, "brown")
dr2 = Dragon(69, 5, "gray")
dr3 = Dragon(88, 8, "green")

print(dr1, dr2, dr3, sep = "\n")
print(dr1 + dr3)
print(dr1-2)
dr1.change_color("white")
dr1.__str__()
dr1.__repr__()
dr1.output('welcome')
print (dr1 > dr2, dr1 != dr2, dr1 <= dr2)

   # def __cmp__(self, other):
    #     return self > other
