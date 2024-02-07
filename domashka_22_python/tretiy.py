class Airplane:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        return self.max_passengers == other.max_passengers

    def __add__(self, other):
        return Airplane(self.max_passengers + other.max_passengers)

    def __sub__(self, other):
        return Airplane(abs(self.max_passengers - other.max_passengers))

    def __iadd__(self, other):
        self.current_passengers += other
        if self.current_passengers > self.max_passengers:
            self.current_passengers = self.max_passengers
        return self

    def __isub__(self, other):
        self.current_passengers -= other
        if self.current_passengers < 0:
            self.current_passengers = 0
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return f"Airplane max ={self.max_passengers}, current={self.current_passengers})"


plane1 = Airplane(100)
plane2 = Airplane(200)
plane3 = Airplane(150)


if plane1 < plane2:
    print(plane1, "has fewer than", plane2)
if plane2 > plane3:
    print(plane2, "has more than", plane3)


plane4 = plane1 + plane2
plane5 = plane4 - plane3


plane1 += 10
plane2 -= 20

print(plane1)
print(plane2)
print(plane4)
print(plane5)