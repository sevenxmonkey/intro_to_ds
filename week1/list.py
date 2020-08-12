list1 = []
for number in range(0, 10):
    if number % 2 == 0:
        list1.append(number)
print(list1)

# Now the same thins but with list comprehension
list2 = [number for number in range(0, 10) if number % 2 == 0]
print(list2)