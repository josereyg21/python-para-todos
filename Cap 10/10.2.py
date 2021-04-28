l = {}
o = []
oo = []
c = input('Archivo: ')
cc = open(c)
for i in cc:
    if i.startswith('From '):
        ii = i.split()
        o.append(ii[5:6])
        for u in o:
           kk = "".join(u)
           oo.append(kk[0:2])

for yy in oo:
    l[yy] = l.get(yy,0) + 1

for h, g in l.items():
    print(h,g)



            
            