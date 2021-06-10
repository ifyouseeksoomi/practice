# What is Enumerate?
data = enumerate((1, 2, 3))
print(data, type(data))
print()
# <enumerate object at 0x7f9b42c27bc0> <class 'enumerate'>

# Case 1. Tuple
data = enumerate((1, 2, 3))
for i, v in data:
    print(i, ":", v)
print()
# 0 : 1
# 1 : 2
# 2 : 3

# Case 2. Set (집합)
data = enumerate({1, 2, 3})
for i, v in data:
    print(i, ":", v)
print()
# 0 : 1
# 1 : 2
# 2 : 3

# Case 3. List
data = enumerate([1, 2, 3])
for i, v in data:
    print(i, ":", v)
print()
# 0 : 1
# 1 : 2
# 2 : 3

# Case 4. Dictionary
dict1 = {'이름': '한사람', '나이': 33}
data = enumerate(dict1)
for i, k in data:
    print(i, ":", k, dict1[k])
print()
# 0 : 이름 한사람
# 1 : 나이 33

# Case 5. String
data = enumerate("재미있는 파이썬")
for i, v in data:
    print(i, ":", v)
print()
# 0 : 재
# 1 : 미
# 2 : 있
# 3 : 는
# 4 :
# 5 : 파
# 6 : 이
# 7 : 썬
