# 다마고치 클래스

# 먹이 투입 하면 건강 수치가 올라감

class Damagochi:



    def __init__(self, name, age, feed_count=0, health=5, ddong=0):
        self.name = name
        self.age = age
        self.feed_count = feed_count
        self.health = health
        self.ddong = ddong

    def eat(self):
        self.feed_count -= 1
        self.health += 1

    def get_ddong(self):
        self.feed_count -= 5
        self.ddong += 1


damagochi1 = Damagochi('뚠뚠이', 4)
damagochi2 = Damagochi('뿡뿡이', 3)

damagochi1.get_ddong()
damagochi2.get_ddong()

print(damagochi1.name, damagochi1.feed_count, damagochi1.health)
print(damagochi2.name, damagochi2.feed_count, damagochi2.health)

