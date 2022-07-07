from typing import List


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self):
        self.__table: List[Node] = [None] * 10
        self.__size = 0

    def hash_func(self, key):
        h = hash(key)
        return h % len(self.__table)

    def insert(self, key, value):
        if key in self:
            raise ValueError()
        index = self.hash_func(key)
        p = Node(key, value)
        if self.__table[index] is None:
            self.__table[index] = p
        else:
            t = self.__table[index]
            while t.next is not None:
                t = t.next
            t.next = p
        self.__size += 1

    def __contains__(self, key):
        index = self.hash_func(key)
        p = self.__table[index]
        while p is not None:
            if p.key == key:
                return True
            p = p.next
        return False

    def __getitem__(self, key):
        if key not in self:
            raise ValueError()
        index = self.hash_func(key)
        p = self.__table[index]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None

    def get_keys(self):
        arr_keys = []
        for line in self.__table:
            p = line
            while p is not None:
                arr_keys.append(p.key)
                p = p.next
        return arr_keys

    def get_values(self):
        arr_values = []
        for line in self.__table:
            p = line
            while p is not None:
                arr_values.append(p.value)
                p = p.next
        return arr_values

    def rehash(self):
        if self.__size / len(self.__table) >= 0.8:
            arr_keys = self.get_keys()
            arr_values = self.get_values()
            for key in arr_keys:
                self.delete(key)
            self.__table += [None] * 5
            for i in range(len(arr_keys)):
                self.insert(arr_keys[i], arr_values[i])

    def __setitem__(self, key, value):
        pass

    def delete(self, key):
        if key not in self:
            return False
        index = self.hash_func(key)
        p = self.__table[index]
        if p.next is None:
            self.__table[index] = None
            self.__size -= 1
            return True
        while p.next is not None:
            if p.next.key == key or p.key == key:
                k = p.next
                p.next = k.next
                return True
            p = p.next

        # k = None
        # while p is not None:
        #     if k is None:
        #
        #
        #     if p.key == key:
        #         k.next = p.next
        #         return True
        #     k = p
        #     p = p.next

    # функция рехеширования (когда кол-во эл-тов = 80% от размеров списка)
    # функция удаления по ключу
    # функции получения списка ключей и списка значений
    # set_item


table = HashTable()
table.insert('apple', 4)
table.delete('apple')
