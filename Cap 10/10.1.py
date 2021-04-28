l = {}
o = []
c = input('Archivo: ')
cc = open(c)
for i in cc:
    if i.startswith('From '):
        ii = i.split()
        o.extend(ii[1:2])
        for e in o:
            l[e] = l.get(e, 0) + 1

pp = None
nn = None
for w, q in l.items():
    if nn is None or q > nn:
        pp = w
        nn = q

print(pp,nn)

