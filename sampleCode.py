s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagram")

dit = {}
for i in s1:
    dit[i] = dit.get(i, 0) + 1

dit2 = {}
for i in s2:
    dit2[i] = dit2.get(i, 0) + 1

for key in dit.keys():
    if dit[key] != dit2.get(key):
        print("Not Anagram")
else:
    print("Anagram")

