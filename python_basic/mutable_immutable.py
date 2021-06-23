# mutable vs. immutable 내가 이해한 것이 맞는지 검증해보기

# verification case 1) mutable object (call by reference)
def mutable_verification(test_list):
    # mutable types : list, dictionary, set (go with 'list')
    test_list += [100]
    print(test_list)
    print(id(test_list))


test_list = [1, 2, 3, 4, 5]
x = test_list

print(test_list)  # --> 1
print(id(test_list))  # --> 2

mutable_verification(test_list)  # --> 3, 4
print(x)  # --> 5
print(id(x))  # --> 6

# 이해한대로 예상해보기
# mutable객체인 리스트는 리스트의 속성값을 변경시킬 수 있다. 이 말은 초기에 할당받은 주소값의 변화 없이 value 변화가 가능하다는 것이다.
# 따라서 1 != 3 == 5 일것이나 2 == 4 == 6 일 것이다.

# 실제 결과
# [1, 2, 3, 4, 5]
# 140675259118048
# [1, 2, 3, 4, 5, 100]
# 140675259118048
# [1, 2, 3, 4, 5, 100]
# 140675259118048

# 옳은 예상


# verification case 2) Immutable object (call by value)
def immutable_verification(test_string):
    # immutable types : string, tuple, int
    test_string += 'finally'
    print(test_string)
    print(id(test_string))


test_string = 'I finished the job'
y = test_string

print(test_string)  # --> a
print(id(test_string))  # --> b

immutable_verification(test_string)  # --> c, d
print(y)  # --> e
print(id(y))  # --> f

# 이해한대로 예상해보기
# immutable 객체인 스트링은 스트링의 속성값을 변경시킬 수 없다. 따라서 만일 새로운 무언가가 추가되거나 변경시키고 싶다면
# 아예 새로운 주소값과 바인딩되는 또 다른 변수를 선언하게 된다. 이 과정에서 기존에 할당되었던 변수는 참조 카운팅이 없어지고 자연히 Garbage collected 될 것이다.
# 따라서 a == e != c 이고 b == f != d일 것

# 실제 결과
# I finished the job
# 140290325600416
# I finished the jobfinally
# 140290325603232
# I finished the job
# 140290325600416

# 옳은 예상
