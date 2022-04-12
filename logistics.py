from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def add(self, name, count):       # ( < название >, < количество >) - увеличивает запас items
        pass

    @abstractmethod
    def remove(self, name, count):     # ( < название >, < количество >) - уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self):          # - вернуть количество свободных мест
        pass

    @abstractmethod
    def get_items(self):               # - возвращает сожержание склада в словаре {товар: количество}
        pass

    @abstractmethod
    def get_unique_items_count(self):  # - возвращает количество уникальных товаров.
        pass