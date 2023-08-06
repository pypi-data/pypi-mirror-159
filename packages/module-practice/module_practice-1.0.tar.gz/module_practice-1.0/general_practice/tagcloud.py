
import sys
from fizbuzz import fizz_buzz_game


class TagCloud:
    def __init__(self):
        self.variabe = 10
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, key):
        return self.__tags.get(key.lower(), 0)

    def __setitem__(self, key, count):

        self.__tags[key.lower()] = count

    def get_item(self, key):
        return self.__getitem__(key=key)

    def set_item(self, key, value):
        try:
            self.__setitem__(key=key, count=int(value))
        except ValueError:
            print("Invalid value")

    def __len__(self):
        return len(self.__tags)


# cloudtag = TagCloud()
# cloudtag.add("python")
# cloudtag.add("java")
# cloudtag.add("pytHon")
# cloudtag.set_item("charp", 10)
# print(cloudtag.get_item("java"))
# print(cloudtag.get_item("CHARP"))
# print(len(cloudtag))
