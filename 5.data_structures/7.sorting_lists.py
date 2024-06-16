items = [
    ("apple",12),
    ("banana",11),
    ("orange",13)
]

def sort_item(item):
    return item[1]

#items.sort(key=item[1])   #error
items.sort(key=sort_item)
print(items)