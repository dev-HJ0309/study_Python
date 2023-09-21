class Gunfire:
    def __init__(self, gun_name, bullet_count=10, fire_count=0):
        self.gun_name = gun_name
        self.bullet_count = bullet_count
        self.fire_count = fire_count

    def fire(self, sniper):
        sniper.score = 100 +(fire_count * 10)
        self.fire_count +=1
        self.bullet_count -= 1

class Sniper:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

sniper = Sniper('주현진', 32, 1000)


print(sniper.sniper.score)

