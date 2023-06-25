class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        occurences = {n: my_list.count(n) for n in my_list}
        occurence = max(occurences, key=occurences.get)
        return occurence

    @classmethod
    def doubles(cls, my_list: list):
        occurences = {n: my_list.count(n) for n in my_list}
        count = sum(value >= 2 for value in occurences.values())
        return count


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
