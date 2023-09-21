class ServiceManual:

    def __init__(self, location, *manager):
        self.location = location
        self.manager = manager



    def greet(self):
        print(f'전화주셔서 감사합니다. 사보텐 {self.location}점 매니저 {self.manager} 입니다. ')

선릉점_manager = ('주현진', '고아라', '차은우')

선릉점 = ServiceManual('선릉', *선릉점_manager)

선릉점.greet()

for manager in 선릉점_manager:
    print(manager)

# 왜 매니저 이름 3개가 다 출력 되는가???


