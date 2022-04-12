from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):  # ( < название >, < количество >) - увеличивает запас items
        pass

    @abstractmethod
    def remove(self, name, count):  # ( < название >, < количество >) - уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self):  # - вернуть количество свободных мест
        pass

    @abstractmethod
    def get_items(self):  # - возвращает сожержание склада в словаре {товар: количество}
        pass

    @abstractmethod
    def get_unique_items_count(self):  # - возвращает количество уникальных товаров.
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    @property
    def add(self, name, count):  # ( < название >, < количество >) - увеличивает запас items
        is_found = False
        if self.get_free_space() >= count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, т.к. нет свободного места")


    @property
    def remove(self, name, count):  # ( < название >, < количество >) - уменьшает запас items
            for key in self.items.keys():
                if name == key:
                    if self.items[key] - count >= 0:
                        self.items[key] = self.items[key] - count
                    else:
                        print(f"{name} слишком мало на складе")
                else:
                    print(f"Нет такого товара на складе")

    @property
    def get_free_space(self):  # - вернуть количество свободных мест
        return self.capacity - sum(self.items.values())

    @property
    def get_items(self):  # - возвращает сожержание склада в словаре {товар: количество}
        return self.items

    @property
    def get_unique_items_count(self):  # - возвращает количество уникальных товаров.
        return len(self.items.keys())


