# 동물 클래스 만들기
# 동물 이름, 동물 나이, 동물 성별/ 음식 개수, 체력 개수
# 먹기, 산책하기

# 먹기: 음식 1개 소진, 체력 1개 획득
# 산책 하기: 음식 1개 획득, 체력 1개 소진

# class Animal:
#     def __init__(self, name=None, age=1, gender="male", feed=0, health=0):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.feed = feed
#         self.health = health
#
#     def eat(self):
#         if self.feed > 0:
#             print(f"{self.name}이(가) 음식을 먹습니다.")
#             self.feed -= 1
#             print(f"남은 음식: {self.feed}")
#         else:
#             print("음식이 부족합니다.")
#     def walk(self):
#         if self.health > 0:
#             print(f"{self.name}이(가) 산책합니다.")
#             self.feed += 1
#             self.health -= 1
#             print(f"남은 체력: {self.health}")
#             print(f"남은 음식: {self.feed}")
#         else:
#             print("체력이 부족합니다.")
#
# tiger = Animal('호랑이', 23, 암컷)
# elephant = Animal('코끼리', 34, 수컷)





# 강사님 풀이
# 동물
# 이름, 나이, 성별, 음식개수, 체력개수
# 먹기, 산책하기

# 먹기: 음식 1개 소진, 체력 1개 획득
# 산책하기: 음식 1개 획득, 체력 1개 소진
class Animal:
    def __init__(self, name, age, gender, food_count=0, health=10):
        self.name = name
        self.age = age
        self.gender = gender
        self.food_count = food_count
        self.health = health
    # 여기까지 초기화
    def eat(self):
        self.food_count -= 1
        self.health += 1

    def walk(self):
        self.food_count += 1
        self.health -= 1


tiger = Animal('호랑이', 23, '암컷')
elephant = Animal('코끼리', 56, '수컷')

tiger.walk()
elephant.walk()

print(tiger.name, tiger.food_count, tiger.health)
print(elephant.name, elephant.food_count, elephant.health)








