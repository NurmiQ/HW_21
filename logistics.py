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
    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        pass

    @abstractmethod
    def get_unique_items_count(self):  # - возвращает количество уникальных товаров.
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

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

    def remove(self, name, count):  # ( < название >, < количество >) - уменьшает запас items
        is_found = False
        for key in self.items.keys():
            if name == key:
                is_found = True
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"{name} слишком мало на складе")
        if not is_found:
            print(f"Нет такого товара на складе")

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.capacity - sum(self.items.values())

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров.
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self.limit = limit

    @property
    def get_item_limit(self):
        return self.limit

    def add(self, name, count):  # ( < название >, < количество >) - увеличивает запас items
        if self.get_unique_items_count() <= self.limit:
            super().add(name, count)
        else:
            print(f"Товар не может быть добавлен")


class Request:
    def __init__(self, str):
        lst = self.get_info(str)
        self.from_ = lst[4]
        self.amount = int(lst[1])
        self.product = lst[2]

        if len(lst) > 6:
            self.to = lst[6]
        else:
            self.to = None

    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить** {self.amount} {self.product} **из** {self.from_} **в** {self.to}'


