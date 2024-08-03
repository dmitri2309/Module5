class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floor + other)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floor += other
            return House(self.name, self.number_of_floor)

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floor + other)


h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)

print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)


class Test:
    def __init__(self, x):
        self.x = x
        # self.y = y

    def __sub__(self, other):
        return self.x - other

    def __mul__(self, other):
        return self.x * other

    def __rsub__(self, other):
        return other - self.x

    def __isub__(self, other):
        self.x -= other
        return self.x

    def __imul__(self, other):
        self.x *= other
        return self.x

    def __mod__(self, other):
        return self.x % other

    def __pow__(self, other):
        return self.x ** other

    def __rpow__(self, other):
        return other ** self.x

    def __truediv__(self, other):
        return self.x / other

    def __floordiv__(self, other):
        return self.x // other


res = Test(6)
print(res - 4)
print(res * 5)
print(4 - res)
res -= 4
print(res)
res *= 3
print(res)
print(res % 4)
print(res ** 2)
print(2 ** res)
print(res / 3)
print(res // 3)
