
a = [['в', 3, 25], ['п', 2, 15], ['б', 2, 15], ['а', 2, 20], ['и', 1, 5], ['н', 1, 15], ['т', 3, 20], ['о', 1, 25],
     ['ф', 1, 15], ['д*', 1, 10], ['к', 2, 20], ['р', 2, 20]]


ed = []
for i in range(len(a)):
    b = int(a[i][2]) // int(a[i][1])
    ed.append(b)

e = [[ed[i], a[i][0], a[i][2]] for i in range(len(a))]
for i in range(len(a)):
    if int(a[i][1]) >= 2:
        e.append([ed[i], a[i][0], 0])

for i in range(len(a)):
    if int(a[i][1]) >= 3:
        e.append([ed[i], a[i][0], 0])

ew = sorted(e, reverse=True)

size = []
h = 1
for s in range(len(ew)):
    if ew[s][1] == 'д*':
        size.append([ew[s][1]])
    if len(size) < 7:
        h += 1
        size.insert(h, [ew[s][1]])

for j in range(0, len(size), 2):
    print('[%s]' % ', '.join(map(str, size[j])),'[%s]' % ', '.join(map(str, size[j + 1])))

summi = 10
for t in range(len(size)):
    summi += int(ew[t][2])

for t in range(8, len(ew)):
    summi -= int(ew[t][2])

print(summi)