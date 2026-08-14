fruits = {"яблоко", "банан"}
fruits.add("апельсин")
print(fruits)
fr_2 = {"груша", "виноград"}
fruits.update(fr_2)
print(fruits)
fruits.discard("банан")
print(fruits)
fruits.discard("киви")
print(fruits)
# fruits.remove("киви")
# print(fruits)
rem_el = fruits.pop()
print(rem_el, "\n")

coord = (10, 20, 30, 20, 10, 20, 40)
print(coord)
print(coord[1])
print(coord[-1:])
print(coord[1:5])
print("30" in coord)
print(coord.index(20))
print(coord.count(20))
print(coord.count(50))
print(len(coord))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]
tup3 = tuple1 + tuple2
print(tup3)
tup4 = tuple1 * 3
print(tup4)
a, b, c = tuple1
print(a)
print(b)
print(c, "\n")

numbers_tuple = tuple(numbers)
first = numbers_tuple[0:1]
middle = numbers_tuple[1:4]
last = numbers_tuple[-1:]
print(first)
print(middle)
print(last, "\n")

numbers_tuple = tuple(numbers)
print(numbers_tuple, "\n")

even = tuple(x for x in range(11) if x % 2 == 0)
print(even, "\n")

sqrt = tuple(x ** 2 for x in range(1, 6))
print(sqrt, "\n")

single_tuple = 42
print(single_tuple, "\n")
