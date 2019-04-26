a = {"1","2","4","5"}
b = {"1","2","6","7"}

i = a.intersection(b)
a = a|b
r = a-i

print(r)
