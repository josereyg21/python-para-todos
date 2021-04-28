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
            
print(u)