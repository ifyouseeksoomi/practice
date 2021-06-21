
# 유튜브 소놀코딩 파이썬 중급강의 3강 '클래스 이해하기 (1)'
# class : '사용자가 정의하는 새로운 자료형' int, str 이런거 말고
class Person:
    def __init__(self):  # 클래스 안의 속성을 초기화할 때 사용하는 생성자/초기자
        self.name = '홍길동'
        self.age = 25
        # 상기의 과정이 바로 초기화


Person()
# 실행 시 아무것도 나오지 않음. 당연.

p = Person()
print(p.name)  # 홍길동
print(p.age)  # 25

# p1 = Person('홍길동', 25)
# p2 = Person('김철수', 33)
# print(p2.name)
# print(p2.age)
# 당연히 에러 뜸
# TypeError: __init__() takes 1 positional argument but 3 were given

# 아래와 같이 수정 코딩한다


class Person2:
    def __init__(self, name, age):  # 고정하지 말고, 매개변수로 전달해버림
        self.name = name
        self.age = age
        # '='를 기준으로 좌변은 '인스턴스 변수', 우변은 '매개변수'라고 일컬음


p2 = Person2('김철수', 33)
# 이 때 Person 객체에 '김철수', 33을 넣어 초기화한다 라고 표현함
print(p2.name)  # 25
print(p2.age)  # 33

# --------------------------------------------------------------------------

# 유튜브 소놀코딩 파이썬 중급강의 4강 '클래스 이해하기 (2)'
# __init__ def 말고 (초기자) 다른 메소드 넣어보기


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp(self):
        print(self.name, self.age)


p3 = Person3('홍길동', 25)
p3.disp()
# 홍길동 25


# --------------------------------------------------------------------------
# 유튜브 소놀코딩 파이썬 중급강의 5강 '클래스 이해하기 (3)'

# class Person4:
#     def __init__(self):
#         self.name = input('이름: ')
#         self.age = int(input('나이: '))  # input 함수의 기본형은 str

#     def disp(self):
#         print(self.name+': '+str(self.age))
#         # print(self.name, ': ', self.age)와 결과가 같은듯 다름 왜냐면 한칸씩 기본적으로 띄어지는게 이 안에는 적용되니깐


# li = []
# for i in range(3):
#     li.append(Person4())

# # 3번에 걸쳐 Person4 객체가 생성되며 생성된 객체의 이름과 나이가(disp 메소드) list에 채워질 것이다
# for i in li:
#     i.disp()  # 이 부분을 print(i)로 할 수도 있겠으나 이미 disp()에 print가 있음. 효율적으로!

# --------------------------------------------------------------------------
# 유튜브 소놀코딩 파이썬 중급강의 6강 '클래스 접근제한자 '__'(던더바)'


class Sj:
    def __init__(self):
        self.kor = 98
        self.eng = 100
        self.math = 88
        self.__art = 90

    def dis(self):
        print(self.__art)

    def getart(self):
        return self.__art

    def setart(self, art):
        self.__art = art


s1 = Sj()
print(s1.math)
# print(s1.art)
# self.__art (던더바 접근제한자를 넣으면)
# AttributeError: 'Sj' object has no attribute 'math' (클래스 밖에서는 해당 속성에 접근할 수 없게된다)
s1.dis()
# 90 (그러나 같은 클래스의 메소드로 호출할 경우, 같은 클래스 내이므로 호출이 된다!)

s1.setart(100)
# 접근제한자로 클래스내에서 선언된 art더라도 이렇게 setter 함수를 활용해서 다시 세팅을 하면

print(s1.getart())
# 100 (getter 함수를 이용하면 방금전에 세팅한 값으로 클래스 밖에서도 해당 속성에 접근할 수가 있게 된다)
