from functools import reduce

items = [11,12,13]

total = reduce(lambda a,b:a+b,items)
print(total)