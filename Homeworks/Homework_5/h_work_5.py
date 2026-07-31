fruits = ["яблоко"]
print(fruits)
fruits.extend(["апельсин", "груша"])
print(fruits)
fruits.append("банан")
print(fruits)
fruits.insert(1, "виноград")
print(fruits, "\n")

fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits)
fruits.remove("банан")
print(fruits)
end_fruits = fruits.pop()
print(end_fruits, "\n")

fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index('банан'))
print(fruits.count('банан'), "\n")

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
