items = [
    ("apple",12),
    ("banana",11),
    ("orange",13)
]

# syntax 
# lambda parammetes:expression


items.sort(key=lambda item:item[1])
print(items)