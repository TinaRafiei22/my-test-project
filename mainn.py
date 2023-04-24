import math
class point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def reset(self) -> None:
            self.move(0 ,0)
    def calcaulate_distance(self, other: "point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

point1 = point()
point2 = point()

point.reset()
point2.move(5, 0)
print(point2.calcaulate_distance(point2))
point2.calcaulate_distance(point1) == point1.calcaulate_distance(point2)

point1.move(3, 4)
print(point1.calcaulate_distance(point2))

print(point1.calcaulate_distance(point1))