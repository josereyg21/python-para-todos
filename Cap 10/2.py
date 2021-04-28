d = {}
f = input('Archivo: ')
e = open(f)
for x in e:
    xx = x.split()
    for xxx in xx:
        d[xxx] = d.get(xxx, 0) + 1

lol = []
for d1, d2 in d.items():
    xs = (d2, d1)
    lol.append(xs)

lol = sorted(lol, reverse=True)

for x, y in lol[:10]:
    print(x,y)