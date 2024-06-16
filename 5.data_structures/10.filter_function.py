items = [
    ("apple",12),
    ("banana",11),
    ("orange",13)
]


prices = list(filter(lambda item:item[1]>12,items))
print(prices)