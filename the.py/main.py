# bubble compare with neighbour element

topping = ["onion", "tomato", "bacon", "paprika", "cheese"]
n = len(topping)

for i in range(n):
    for j in range(0, n - i - 1):
        if topping[j] > topping[j + 1]:
            topping[j], topping[j + 1] = topping[j + 1], topping[j]

print("sorted topping:", topping)


#selection sort take a min index

topping = ["onion", "tomato", "bacon", "paprika", "cheese"]
n = len(topping)

for i in range(n):
    min=i
    for j in range(i+1, n):
        if topping[j] < topping[min]:
            min = j
    topping[i], topping[min]=topping[min], topping[i]
print("sort toping:", topping)

