file = open("input\input19.txt")
l = file.read().split("\n")
file.close()

patterns = set(l[0].split(", "))
# print(f'{ps= }')

r = 0
for design in l[2:]:
    pos = [False] * (len(design) + 1)
    pos[0] = True

    for i in range(1, len(design) + 1):
        for j in range(i):
            if pos[j]:
                print(f'{i= }, {j= }, {design[j:i]= }')
                if design[j:i] in patterns:
                    pos[i] = True
                    break

    r += pos[-1]
    break

print(r)