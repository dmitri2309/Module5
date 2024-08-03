class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'

    def __lt__(self, other):
        return self.number_of_floor < other

    def __gt__(self, other):
        return self.number_of_floor > other

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other

    def __le__(self, other):
        return self.number_of_floor <= other

    def __ge__(self, other):
        return self.number_of_floor >= other

    def __ne__(self, other):
        return self.number_of_floor != other

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
