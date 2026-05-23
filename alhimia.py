from functools import lru_cache

class Elem:
    _reactions = {
        ("Огонь", "Вода"): "Пар",
        ("Вода", "Огонь"): "Пар",
        ("Огонь", "Пар"): "Плазма",
        ("Пар", "Огонь"): "Плазма",
    }

    def __init__(self, name):
        self.name = name

    @staticmethod
    @lru_cache(maxsize=None)
    def _make_key(name1, name2):
        return tuple(sorted([name1, name2]))

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_reaction(name1, name2):
        key = Elem._make_key(name1, name2)
        reaction_map = {
            ("Вода", "Огонь"): "Пар",
            ("Огонь", "Пар"): "Плазма",
        }

        return reaction_map.get(key)

    def __add__(self, other):
        if not isinstance(other, Elem):
            raise TypeError(f"Cannot combine Elem with {type(other)}")

        result_name = self._get_reaction(self.name, other.name)

        if result_name:
            print(f"{self.name} + {other.name} = {result_name}")
            return create_element(result_name)
        else:
            print(f"Ничего не произошло! {self.name} + {other.name} не дают нового элемента.")
            return None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Elem('{self.name}')"


class Fire(Elem):
    def __init__(self):
        super().__init__("Огонь")


class Water(Elem):
    def __init__(self):
        super().__init__("Вода")


class Steam(Elem):
    def __init__(self):
        super().__init__("Пар")


class Plas(Elem):
    def __init__(self):
        super().__init__("Плазма")


def create_element(name):
    elements_map = {
        "Огонь": Fire,
        "Вода": Water,
        "Пар": Steam,
        "Плазма": Plas,
    }
    if name in elements_map:
        return elements_map[name]()
    else:
        return Elem(name)


class Game:
    def __init__(self):
        self.elements = set()
        self.discovered_reactions = set()
        self.starting_elements = ["Огонь", "Вода"]

        for elem_name in self.starting_elements:
            self.add_element(create_element(elem_name))

        print("Добро пожаловать в игру Алхимия!")
        print(f"Начальные элементы: {', '.join(self.starting_elements)}")
        print("Комбинируйте элементы, чтобы создавать новые!")
        print("Введите 'список' для просмотра элементов, 'выход' для выхода\n")

    def add_element(self, element):
        if element and element.name not in [e.name for e in self.elements]:
            self.elements.add(element)
            print(f"Открыт новый элемент: {element.name}!")
            return True
        return False

    def combine_elements(self, elem1, elem2):
        if not isinstance(elem1, Elem) or not isinstance(elem2, Elem):
            print("Ошибка: Оба аргумента должны быть элементами!")
            return None

        result = elem1 + elem2

        if result:
            self.add_element(result)
            pair = tuple(sorted([elem1.name, elem2.name]))
            self.discovered_reactions.add(pair)
        return result

    def list_elements(self):
        if not self.elements:
            print("У вас пока нет элементов!")
            return

        print("\nВаши элементы")
        sorted_names = sorted([e.name for e in self.elements])
        for i, name in enumerate(sorted_names, 1):
            print(f"{i}. {name}")
        print(f"Всего элементов: {len(self.elements)}\n")


    def get_element_by_name(self, name):
        for elem in self.elements:
            if elem.name.lower() == name.lower():
                return elem
        return None

    def play(self):
        while True:
            print("\n" + "=" * 40)
            command = input("Введите команду (комбинация/список/выход): ").strip().lower()

            if command == "выход":
                print(f"Игра окончена! Вы открыли {len(self.elements)} элементов.")
                break

            elif command == "список":
                self.list_elements()

            elif command == "комбинация":
                if len(self.elements) < 2:
                    print("У вас недостаточно элементов для комбинации!")
                    continue

                print("Доступные элементы:")
                elements_list = list(self.elements)
                for i, elem in enumerate(elements_list, 1):
                    print(f"{i}. {elem.name}")

                try:
                    choice1 = int(input("Выберите первый элемент (номер): ")) - 1
                    choice2 = int(input("Выберите второй элемент (номер): ")) - 1

                    if 0 <= choice1 < len(elements_list) and 0 <= choice2 < len(elements_list):
                        elem1 = elements_list[choice1]
                        elem2 = elements_list[choice2]
                        self.combine_elements(elem1, elem2)
                    else:
                        print("Неверный номер элемента!")
                except ValueError:
                    print("Пожалуйста, введите число!")

            else:
                print("Неизвестная команда! Используйте: комбинация, список, возможные, выход")


if __name__ == "__main__":
    game = Game()
    game.play()