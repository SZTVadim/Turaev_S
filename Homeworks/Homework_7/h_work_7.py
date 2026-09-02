fruits = {"яблоко", "банан"}
fruits_2 = {"груша", "виноград"}

fruits.add("апельсин")
print(fruits, "\n")

fruits.update(fruits_2)
print(fruits, "\n")

fruits.discard("банан")
print(fruits, "\n")

fruits.discard("киви")
print(fruits, "\n")

# fruits.remove("киви")
# print(fruits, "\n")

delfruits = fruits.pop()
print(delfruits, "\n")


coord = (10, 20, 30, 20, 10, 20, 40)
print(coord)
print(coord[0])
print(coord[-1])
print(coord[1:4])
print(30 in coord)
print(coord.index(20))
print(coord.count(20))
print(coord.count(50))
print(len(coord))
