# 지하철 요금 메소드
# 기본 요금 1300원
# 출발지에서 15정거장 이후 부터 1정거장 마다 100원 추가 금액 발생
# 거리에 따른 요금 계산 메소드
# 거리에 따른 잔돈 계산 메소드

class Subway:
    init_fare = 1300
    init_distance = 15
    over_charge = 100
    over_charge
    def __init__(self, money, distance):
        self.money = money
        self.distance = distance
    # 여기까지 초기화

    # 거리에 따른 요금 계산
    def set_cost(self):
        cost = Subway.init_fare
        if self.distance > Subway.init_distance:
            cost += (self.distance - Subway.init_distance) * over_charge

        return cost

    # 거리에 따른 잔돈 계산
    def get_change(self):
        change = self.money - self.set_cost()
        return change

    jhj = Subway(12000, 22)
    hgd = Subway(15000, 33)

    print(jhj.set_cost(), jhj.get_change())
    print(hgd.set_cost(), hgd.get_change())