maps = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for item in maps:
    print(item)

point = str(input("Select your point for find GOLD: like this: 12, 1 is means row and 2 is means col\n"))
print(maps[int(point[0])][int(point[1])])