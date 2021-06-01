import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_1165362.txt')

counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)