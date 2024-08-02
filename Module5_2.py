class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        floor_number = 0
        if new_floor < 1 or new_floor > self.number_of_floor:
            print(f'Такого этажа в жилом комплексе {self.name} не существует')
        else:
            while floor_number < new_floor:
                floor_number += 1
                print(floor_number)

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'


h1 = House('"ЖК Горский"', 18)
h2 = House('"Домик в деревне"', 2)
h1.go_to(5)
h2.go_to(10)

h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))
