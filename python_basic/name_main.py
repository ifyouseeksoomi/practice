
# if __name__ == '__main__': << 뭘까 이건
# 해당 모듈이 import된 경우가 아니라, 인터프리터에서 직접 실행된 경우에만 if문 이하의 코드를 돌리라는 뜻.

def func():
    print("function working")


if __name__ == "__main__":
    print("직접 실행")
    print(__name__)
# 이 파일을 저장한 후, python name_main.py 로 바로 실행한 경우 if문 이하의 코드 실행 : 아래의 결과 프린트
# 직접 실행
# __main__
else:
    print("import되어 사용됨")
    print(__name__)
# 이 파일을 저장한 후, python 실행 -> import name_main.py 로 실행한 경우 else문 이하의 코드 실행 : 아래의 결과 프린트
# import되어 사용됨
# name_main (import된 경우 해당 파일의 이름이 출력됨)

# __nameㄱiinterperereter가 실행전에 만들어 둔 글로벌 변수


# reference
# https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720
