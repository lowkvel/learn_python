# c2
a = ['a', 'b', 'c']
print(a[0])
print(a[-1])

# append
a.append("d")
print(a)

# insert
a.insert(1, "temp")
print(a)

# delete - del
del a[1]        # del position
print(a)

# delete - pop
s = a.pop()     # pop last
print(a)
print(s)

s = a.pop(1)    # pop position
print(a)
print(s)

# delete - remove
a.remove("c")   # only the first occurrence of the value specified got removed
print(a)

# sort - permanently change the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sort - temporarily change the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)



