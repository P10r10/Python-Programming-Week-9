class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        total_h = sum([person.height for person in self.persons])
        print(f"There are {len(self.persons)} persons in the room, and their "
              f"combined height is {total_h} cm")
        for person in self.persons:
            print(person)

    def shortest(self):
        if self.is_empty():
            return None
        min_h = 300
        for person in self.persons:
            if person.height < min_h:
                min_h = person.height
                shortest = person
        return shortest

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest = self.shortest()
        self.persons.remove(shortest)
        return shortest


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
