# class
# https://wikidocs.net/16071

class Flight:
    def __init__(self, number):
        self._number = number

    def number(self):
        # 파이썬 메서드의 첫번째 파라미터명은 관례적으로 self를 사용
        # 호출 시, 호출한 객체 자신이 전달되기 때문
        return self._number


f = Flight(5)  # 객체 생성 (생성자)
# 생성자로 객체 생성을 호출받으면,
# 1) __new__를 호출하여 객체를 생성 할당 (__new__는 자동 실행되므로 굳이 명시하지 않아도 OK)
# 2) __new__메소드는 __init__메소드를 호출하여 객체에서 사용할 초기값들을 초기화
# 주의: __init__ 메소드가 생성자는 아님!

print(f)  # <__main__.Flight object at 0x7ff1378b94f0>
print(type(f))  # <class '__main__.Flight'>

print(f.number())
print(f._number)
print(Flight.number(f))

# 파이썬은 기본적으로 다른 언어에 있는 접근제어자 public, private, protected 등이 없다
# 기본적으로 모두 public이다.
