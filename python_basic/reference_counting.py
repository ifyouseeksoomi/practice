import sys
a = []
b = a
print(sys.getrefcount(a))
b = 1
print(sys.getrefcount(a))
