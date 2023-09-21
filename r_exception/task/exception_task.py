# 캐릭터 닉네임 정할 때 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작 하여 발생 시 안내 메세지 까지 출력하기
# 문제를 읽고 두번 생각 해 보고 시작하자, 들여쓰기 신경쓰자




# 희수님 코드
class BadWordError(Exception):
    def __str__(self):
        return "입력하신 단어는 닉네임으로 사용 할 수 없습니다."


def check_bad_word(nickname):
    bad_word = ['바보', '멍게', '해삼', '운영자', ' ']
    for i in bad_word:
        if nickname.__contains__(i):
            raise BadWordError


try:
    nickname = input("캐릭터 닉네임을 입력하세요,\n 비속어 및 공백은 입력이 불가합니다.\n: ")
    check_bad_word(nickname)
    print(f"{nickname}님 환영합니다!")
except BadWordError as e:
    print(e)
    print(f"{nickname}은(는) 사용할 수 없는 닉네임입니다.")


    #  강사님 코드
    # 캐릭터 닉네임 정할 때 비속어를 사용하지 못하게 막아주기
    # 바보 멍게 해삼 운영자
    # 직접 Error를 제작하여 발생 시 안내 메세지까지 출력하기
    # class NickNameError(Exception):
    #     def __str__(self):
    #         return "사용하실 수 없는 닉네임입니다."
    #
    #
    # def check_nickname(nickname):
    #     not_allowed_names = ['바보', '멍게', '해삼', '운영자']
    #     for name in not_allowed_names:
    #         if nickname.__contains__(name):
    #             raise NickNameError
    #
    #
    # nickname = input("닉네임: ")
    #
    # try:
    #     check_nickname(nickname)
    #     print(f'어서오시게, {nickname} 용사')
    #
    # except NickNameError as e:
    #     print(e)