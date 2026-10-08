
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1


a = [Player("Julia")]
b = a.copy()
b[0].name = "Yulia"
print(a is b)
print(a[0].name)
print(b[0].name)

import copy
b = copy.deepcopy(a)
b[0].name = "Iulia"
print(a is b)
print(a[0].name)
print(b[0].name)