name = "Alice"
names = [name, "Bob", "Charlie"]
coordinates = (10.0, 20.0, 30.0)
mixed = [name, 40.0, True]
for i in range(len(name)):
    print(name[i])
for i in range(len(names)):
        print(names[i])
for i in range(len(coordinates)):
        print(coordinates[i])
for i in range(len(mixed)):
        print(mixed[i])

for letter in name:
    print(letter)

for n in names:
    print(n)

for coordinate in coordinates:
    print(coordinate)

for elt in mixed:
    print(elt)
