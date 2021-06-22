# 유튜브 소놀코딩 파이썬 중급강의 7강 '클래스 상속'
class Person:
    def __init__(self):
        self.name = '홍길동'
        self.age = 25

    def say(self):
        print()


class Korean(Person):
    def __init__(self):
        super().__init__()  # 부모(Person)의 초기자를 수행
        self.lang = '한국어'

    def say(self):
        print('안녕하세요.')


class American(Person):
    def __init__(self):
        super().__init__()
        self.lang = '영어'

    def say(self):
        print('hello.')


p1 = Person()
print(p1.name, p1.age)  # 홍길동 25
k1 = Korean()
print(k1.name, k1.age, k1.lang)  # 홍길동 25 한국어
k1.say()
a1 = American()
print(a1.name, a1.age, a1.lang)
a1.say()

# 다형성 개념
# 부모 클래스가 가진 함수를 자식도 가지고 있을 때, (위에서 say()에 해당)
# 자식 함수가 더 먼저 수행된다. (== overriding)

# -----------------------------------------------------------
# 유튜브 소놀코딩 파이썬 중급강의 8강 '상속과 다형성' 예제 풀기


class Point:
    def __init__(self):
        self.x = int(input('x= '))
        self.y = int(input('y= '))

    def disp(self):
        pass  # 자식단에서 상세히 구현할거라 그냥 pass


class Rect(Point):
    def __init__(self):
        super().__init__()
        self.w = int(input('w= '))
        self.h = int(input('h= '))

    def disp(self):
        print('사각형', self.x, self.y, self.w, self.h)


class Circle(Point):
    def __init__(self):
        super().__init__()
        self.r = int(input('r= '))

    def disp(self):
        print('원', self.x, self.y, self.r)


def main():
    li = list()
    while True:
        s = input('1. 사각형 2. 원 3. 조회 4. 종료')
        if s == '1':
            li.append(Rect())
        if s == '2':
            li.append(Circle())
        if s == '3':
            for i in li:
                i.disp()  # print(i)와 같겠다 사실
        if s == '4':
            break


print('프로그램을 종료합니다.')

main()
