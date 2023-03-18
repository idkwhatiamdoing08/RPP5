class Row:
    def __init__(self, num: int):
        self.num = num

    def getnum(self):
        return self.num

    def set_num(self, val):
        self.num = val

class Table(Row):
    def __init__(self,num, articul, name, amount, price):
        super().__init__(num)
        self.articul = articul
        self.name = name
        self.amount = amount
        self.price = price

    def __str__(self):
        return f"{self.num}  {self.articul}  {self.name}  {self.amount}  {self.price}"

    def __repr__(self):
        return f"{self.num}  {self.articul}  {self.name}  {self.amount}  {self.price}"

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class FileHandler:
    def __init__(self, path):
        self.count = 0
        self.path = path
        self.data = self.Fopen(self.path)

    def __str__(self):
        return '\n'.join([str(i) for i in self.data])

    def __repr__(self):
        return f"{[repr(i) for i in self.data]}"

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        if self.count >= len(self.data):
            self.point = 0
            raise StopIteration
        else:
            self.count += 1
            return self.data[self.count - 1]

    def generator(self):
        self.count = 0
        while self.count < len(self.data):
            yield self.data[self.count]
            self.count += 1

    def price_sort(self) -> list:
        return sorted(self.data, key=lambda f: f.price)

    def name_sort(self) -> list:
        return sorted(self.data, key=lambda f: f.name)

    def __getitem__(self, item):
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Такого номера не существует")

    @staticmethod
    def Fopen(path: str) -> list:
        original_data = []

        with open(path, "r") as csvreader:
            for line in csvreader:
                (num, articul, name, amount, price) = line.replace("\n", "").split(",")
                original_data.append(Table(num, articul, name, amount, price))
        return original_data

    def addNewItem(self, num, articul, name, amount, price):
        self.data.append(Table(num, articul, name, amount, price))
        self.Fsave(self.path,self.data)

    def Item_serach(self) -> list:
        return [i for i in self.data if i.price >= "79"]

    @staticmethod
    def Fsave (f, add_data):
        with open(f, "w") as csvfile:
            for element in add_data:
                csvfile.write(f"{element.num},{element.articul},{element.name},{element.amount},{element.price}\n")


d = FileHandler('data.csv')


def Main():
    print("Итератор:")
    for i in iter(d):
        print(i)
    print("Генератор:")
    for i in d.generator():
        print(i)
    print("\nДанные (__repr__):\n", repr(d), sep='\n')
    print("Сортировка по названию товара: ")
    for i in d.name_sort():
        print(i)
    print("Сортировка по цене: ")
    for i in d.price_sort():
        print(i)
    d.addNewItem(input('Номер товара: '), input('Артикул: '),
                 input('Название товара: '), input('Количетсво: '),
                 input('Цена: '))

    print("Товары на складе: ")
    for i in d.Item_serach():
        print(i)
    a = int(input("Введите индекс:"))
    print("Строчка под индексом", a, "->", d.__getitem__(a))

Main()






