a = 1
b = 1
c = 1

print(id(1))  # 140340726208816
print(id(a))  # 140431160645936
print(id(b))  # 140431160645936
print(id(c))  # 140431160645936

a += 1
b = 2

print(a)  # 2
print(b)  # 2
print(id(2))  # 140480731027792
print(id(a))  # 140480731027792
print(id(b))  # 140480731027792
