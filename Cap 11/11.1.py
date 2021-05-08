import re

x = 0
f = input('Dame texto ')
p = open(f)
r = p.read()
o = re.findall('[0-9]+', r)
for k in o:
    c = float(k)
    x = x + c
print(x)