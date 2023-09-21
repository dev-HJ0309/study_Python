import hello

# 실행 대상인 파일의 모듈명 (__name__)이 '__main__' 이라면 실행할 코드 작성
# 여러 개의 모듈을 import 하여 사용 할 떄 가장 처음으로 실행 될 메인 파일을 구분 하는 코드이다.
# 즉, 모듈인지 시작점인지 구분하기 위해 사용한다.
if __name__ == '__main__':
    print('PyCharm')

# if __name__ == '__main__':
#     print('주현진 좋아')