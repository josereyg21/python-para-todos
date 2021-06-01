import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_1165362.txt')
for line in fhand:
    print(line.decode().strip())