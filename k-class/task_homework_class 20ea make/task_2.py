# 팀플 기여도

class 팀플:
    # 단위: 퍼센트
    기여도 = 100

    def __init__(self, 팀원명, 팀원기여도):
        self.팀원별명 = 별명
        self.팀원기여도 = 팀원기여도

    def 기여도계산(self, 팀원기여도):
        팀플.기여도 -= 팀원기여도


주현진 = 팀플("버스운전사", "50")
홍길동 = 팀플("짐짝", "50")

주현진.기여도계산(3)
print(팀플.기여도)

