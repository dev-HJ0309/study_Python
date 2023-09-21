# 직영점, 가맹점
class BurgerKing:
    contry = 'KOR'

    def __init__(self, market_type, location):
        self.market_type = market_type
        self.location = location

    def check(self):
        print(f'버거킹 {self.location}점은 {self.market_type}매장 입니다.')

burgerking = BurgerKing("가맹", "강남")
burgerking.check()









