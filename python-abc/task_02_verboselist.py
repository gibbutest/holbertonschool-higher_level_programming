#!/usr/bin/python3
""" The module """


class VerboseList(list):
    """class extends list class"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, inter):
        super().extend(inter)
        print(f"Extended the list with [{len(inter)}] items")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, i=-1):
        print(f"Popped [{self[i]}] from the list.")
        return super().pop(i)
