class 파리바게트:
    인테리어 = "밝게"

    def __init__(self, 위치, *상품들):
        self.위치 = 위치
        self.상품들 = 상품들

    def 인사박기(self):
        print(f'파리바게트 {self.위치}점을 찾아주신 고객님 어서오세요.')


강남점_상품들 = ('단팥빵', '소보루', '크림빵')

강남점 = 파리바게트('강남', *강남점_상품들)

강남점.인사박기()

for 상품 in 강남점.상품들:
    print(상품)








