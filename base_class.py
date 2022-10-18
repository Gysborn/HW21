from abstract_class import Storage
from exeptions import MissingProductError, NotEnoughSpaceError, RequiredQuantityError


class BaseStorage(Storage):
    def __init__(self, name: str, items: dict, capacity: int, max_unique_items=None):
        self.__items = items
        self.__capacity = capacity
        self.__max_unique_items = max_unique_items
        self.__name = name

    def add(self, name: str, amount: int):
        if name not in self.__items:
            self.__items[name] = amount
            self.__capacity -= amount
        else:
            self.__items[name] += amount
            self.__capacity -= amount

    def remove(self, name: str, amount: int):
        self.__items[name] -= amount
        self.__capacity += amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def check_to(self, name: str, amount: int):  # Проверяет на вместимость склад назначения
        if name not in self.__items:
            if self.__max_unique_items:
                if self.get_unique_items_count >= self.__max_unique_items:
                    raise NotEnoughSpaceError

        if self.__capacity - amount < 0:
            raise NotEnoughSpaceError

    def check_in(self, name: str, amount: int):  # Проверяет на наличие склад отправления
        if name not in self.__items:
            raise MissingProductError
        if self.__items[name] < amount:
            raise RequiredQuantityError

    @property
    def get_free_space(self):
        return self.__capacity

    @property
    def get_items(self):
        return self.__items

    def _get_unique_items_count(self):
        return len(self.__items)

    @property
    def name(self):
        return self.__name

    def revision(self):
        for v in self.__items.values():
            self.__capacity -= v
