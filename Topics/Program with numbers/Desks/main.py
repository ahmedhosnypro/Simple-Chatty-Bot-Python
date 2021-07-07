class1 = int(input())
class2 = int(input())
class3 = int(input())

desks = class1 // 2
desks += class1 % 2

desks += class2 // 2
desks += class2 % 2

desks += class3 // 2
desks += class3 % 2

desks = int(desks)

print(desks)
