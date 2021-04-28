e = None
f = None
o = []
u = {}
l = input('Dame el nombre del archivo:')
p = open(l)
for x in p:
    if x.startswith('From '):
        y = x.split()
        o.extend(y[1:2])
        for h in o:
            u[h] = u.get(h, 0) + 1

for q,t in u.items():
    if f is None or t > f:
        e = q
        f = t

print(e,f)