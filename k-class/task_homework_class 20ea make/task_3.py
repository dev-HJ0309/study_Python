# 포켓몬 클래스
# 포켓몬 이름, 포켓몬 타입, 포켓몬 성별
# 훈련하기, 열매 먹기

# 훈련하기 : 체력 1소진, 경험치 1증가
# 열매먹기 : 열매 1소진, 체력 1증가

class Poketmon:
    def __init__(self, name=None, type="normal", gender="male",fruits=10, hp=0, xp=0):
        self.name = name
        self.type = type
        self.gender = gender
        self.fruits = "fruits"
        self.hp = hp
        self.xp = xp

    def eat(self):
        if self.fruits -= 1
            print(f'{self.name}이(가) 열매를 먹습니다')
            self.fruits -= 1
            print(f'남은 열매는 {self.fruits}개 입니다.')
        else:
            print("열매가 부족합니다.")

    def training(self):
        if  self.hp -= 1
            self.xp += 1
            # print(f"{self.name}이(가) 훈련을 완료 했습니다.")
            #
            #
            # print(f'현재 경험치: {self.xp}')
            # print((f"남은 체력: {self.hp}"))
        # else:
        #     print("체력이 부족합니다.")

    ggobugi = Poketmon('꼬북꼬북', normal, "male")
    pairi = Poketmon('성냥개비', fire, "female")








