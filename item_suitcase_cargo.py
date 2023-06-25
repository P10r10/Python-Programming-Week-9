class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
        self.__total_w = 0  # total weight

    def add_item(self, item: Item):
        if item.weight() + self.__total_w <= self.__max_weight:
            self.__items.append(item)
            self.__total_w += item.weight()

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.__total_w

    def heaviest_item(self) -> Item:
        if self.__total_w == 0:
            return None
        top_weight = 0
        for item in self.__items:
            if item.weight() > top_weight:
                top_weight = item.weight()
                heaviest = item
        return heaviest

    def __str__(self) -> str:
        nb = len(self.__items)  # number of items
        return f"{nb} {'item' if nb == 1 else 'items'} ({self.__total_w} kg)"


class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__suitcases = []
        self.__total_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__total_weight <= self.__max_weight:
            self.__suitcases.append(suitcase)
            self.__total_weight += suitcase.weight()

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self) -> str:
        nb_s = len(self.__suitcases)  # number of suitcases
        return f"{nb_s} {'suitcase' if nb_s == 1 else 'suitcases'}, " \
            f"space for {self.__max_weight - self.__total_weight} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
