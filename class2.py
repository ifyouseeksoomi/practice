# class2
# https://wikidocs.net/16071

# __init__에서 객체의 불변성을 확립하는 것이 좋다
# __init__에서는 객체 생성 시 들어올 값에 대해 Validation을 수행한다

# <규칙>
# 비행기 번호의 앞 두 글자는 영문 대문자여야 한다.
# 뒤에서 세번째 글자부터 마지막까지는 양수여야 한다.

class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("첫 두글자가 알파벳이 아닙니다.")
        if not number[:2].isupper():
            raise ValueError("첫 두글자가 대문자가 아닙니다.")
        if not number[2:].isdigit():
            raise ValueError("세번째 글자 이상이 양의 숫자가 아닙니다.")
        self._number = number

    def number(self):
        return self._number


# f = Flight("abc")
# print(f)  # ValueError: 첫 두글자가 대문자가 아닙니다.

# f = Flight("AB110")
# print(f) # <__main__.Flight object at 0x7feeedc29fd0>

f = Flight("AB110")
print(f._number)  # AB110

f._number = 'abc'
print(f.number())  # abc
# 여기서 알 수 있는 사실
# 언더바 한개는 내부적으로만 사용되는 변수이기도 하지만 사실 값을 얻어오는 것이나 할당도 가능하다.
# 여기서 원천적인 접근을 막으려면 더블 언더바를 사용한다. (_number --> __number)
# 이 경우엔 위에서처럼 값을 얻어오는 것도, 할당도 불가능하다.
# AttributeError: 'Flight' object has no attribute '__number' 출력
