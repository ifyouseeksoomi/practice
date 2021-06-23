# -----------------------------------------------------------
# 유튜브 소놀코딩 파이썬 중급강의 10강 '파일 읽고 쓰기'

# ex 1 : write

f = open('/Users/soomialexhwang/Desktop/pdepression.csv', 'w')
# 파일 객체 f 오픈 시 첫번째 파라미터로는 경로, 두번째로는 모드 (w, r)

for i in range(1, 8):
    f.write('%d번째\n' % i)
f.close()
# pdepression 파일에 원래 있던 내용이 모두 지워지고, 1번째~7번째만 남았다


# ex 2 : read

f = open('/Users/soomialexhwang/Desktop/pdepression.csv', 'r')
m = f.readlines()
f.close()

print(type(f))
# <class '_io.TextIOWrapper'>

print(f)
# <_io.TextIOWrapper name='/Users/soomialexhwang/Desktop/pdepression.csv' mode='r' encoding='UTF-8'>

print(type(m))
# <class 'list'>
# 파일객체를 r 모드로 오픈 한 후 readlines() 메소드를 사용하면 파일 내 모든 객체를 다 읽어 리스트 형태로 반환

print(m)
# ['1번째\n', '2번째\n', '3번째\n', '4번째\n', '5번째\n', '6번째\n', '7번째\n']

for i in m:
    print(i)
# 1번째

# 2번째

# 3번째

# 4번째

# 5번째

# 6번째

# 7번째

for i in m:
    print(i, end='')
# 1번째
# 2번째
# 3번째
# 4번째
# 5번째
# 6번째
# 7번째


# [심화] print()의 인자값 (end, sep, file)
# 줄바꿈 기호 때문에 print의 두번째 인자에 들어간 end=''의 작동법이 헷갈리니 직접 IDLE에서 쉬운 코드로 작업해보기

# [1] end 인자
# print 함수의 마지막 효과를 변경할 수 있음 (여기서 중요한 것 : 마지막 효과의 default는 "개행")

>> > a = ['1 0', '2 0', '3 0']
>> > for i in a:
    print(i)

1 0
2 0
3 0

>> > for i in a:
    print(i, end='')

1 02 03 0

>> > for i in a:
    print(i, end=' ')

1 0 2 0 3 0


# [2] sep 인자
# print 함수에 콤마로 구분되어 주어진 문자열을 sep 인자로 결합할 수 있음

>> > print('hello', 'python', sep='$')
hello$python


# [3] file 인자
# 1) file 값으로 w 모드의 파일 오픈을 넣어주면 해당 파일을 읽어 그 파일에 print()함수에 전달된 인자값을 적는다
# 2) sys 모듈은 기본적으로 파이썬 인터프리터를 제어할 수 있는 방법을 제공
#    그 중 sys.stderr는 인터프리터가 표준 에러에 사용하는 파일 객체 (그래서 file인자 사용)

# 1)
f = open('/Users/soomialexhwang/Desktop/pdepression.csv', 'w')
print('Hello python', file=f)
f.close()

# 경로로 찾아가서 파일 열어서 Hello Python 써버림

# 2)
# import sys

print('hello python', file=sys.stderr)
