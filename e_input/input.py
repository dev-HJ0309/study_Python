# name = input("이름: ")
# # 위에 입력 함수 전체가 값이다.
#
# formatting = "{}님 환영합니다.".format(name)
# print(formatting)




# f 문자열 (3.6버전)
# formatting = f"{name}님 환영합니다."
# print(formatting)
#
# # 제 이름은 ???, 키는 ???cm
# name, height = '주현진', 176.5
# formatting = f'제 이름은 {name}, 키는 {height}cm 입니다.'
# print(formatting)

# 세 정수를 입력 받은 후 곱셈 결과 출력 첫 번째 정수와 두번째 정수 곱 한 후 세번째 정수로 나눠주기
# message1, message2, message3 ="첫 번째 정수: ", "두 번째 정수: ", "세 번째 정수: "
# number1, number2, number3 = int(input(message1)), int(input(message2)), int(input(message3))
#
# result= number1 * number2 / number3
#
# formatting = f"{number1} * {number2} / {number3} = {result}"
# print(formatting)






#
# message1, message2 = "첫 번째 정수: ", "두 번째 정수: "
# number1, number2 = int(input(message1)), int(input(message2))
# result = number1 * number2
# formatting = f"{number1} * {number2} = {result}"
# print(formatting)

a, b, c = "A,B,C".split(",")
print(a, b, c, sep=",")

hour, minute = "10:30".split(":")
print(f'{hour}시 {minute}분')

hour, minute, second = "07:20:15".split(":")
print(f'{hour}시 {minute}분 {second}초')

bike, fruit, machine = "오토바이 바나나 냉장고".split(" ")
print(f"{fruit}를 {machine}에 넣고 {bike}로 배송 해줘")


print("010-1234-1234".split("-"))
print("공주시,도읍면,강안리,22-1동".split(","))

name, age = "한동석 20".split(" ")
print(f'{name}님의 나이는 {age}살')

name, job ="주현진,외식업".split(",")
print(f"{name}님의 직업은 {job}입니다.")

# number1, number2, number3 = input("3개의 정수를 입력하세요.\n예)1 2 3\n").split(" ")
# result = int(number1) + int(number2) + int(number3)
# formatting = f'{number1} + {number2} + {number3} = {result}'
# print(formatting)



number1, number2, number3 =input("지금 생각나는 숫자 3개를 입력 하세요. \n 예) 1-2-4\n").split("-")
result= int(number1) + int(number2) -int(number3)
formatting = f"{number1} + {number2} - {number3}"
print(formatting)





