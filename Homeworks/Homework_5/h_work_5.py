#Case_1
fruits = ['яблоко']
fruits.extend(['апельсин', 'груша'])
fruits.append('банан')
fruits.insert(1,'виноград')
print(fruits,"\n")
#Case_2
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits)
fruits.remove("банан")
print(fruits)
end_fruits = fruits.pop()
print(end_fruits, "\n")
#Case_3
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index('банан'))
print(fruits.count('банан'), "\n")
#Case_4
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
