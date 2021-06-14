# class
# https://wikidocs.net/16071

# 파이썬에는 메소드 오버로딩이 없다.
# 메소드 오버로딩 : 하나의 클래스 내부에서 메소드 명칭은 똑같은데 인자를 다르게 하는 형태를 허용하는 것
# 대표적으로 자바에서는 다음과 같은 코드를 허용한다.
# class Adder{
#     static int add(int a,int b)
#     {
#         return a+b;
#     }
#     static int add(int a,int b,int c)
#     {
#         return a+b+c;
#     }
# }

class Korea:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )

    def show(self, abc):
        print('abc: ', abc)


k = Korea('대한민국', 5000000, '서울')
k.show()
# TypeError: show() missing 1 required positional argument: 'abc'

# 위의 결과로, 처음 선언한 show(self)는 무시되고, show(self, abc)만 실행되는 것을 알 수 있다.
