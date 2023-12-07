#유저한테 과일 이모지 다섯개를 입력받고
#랜덤으로 해당 과일을 뽑아서
#~~과일은 맛있죠!
import random

fruits = []


a=input("과일을 입력하세요: \n")
fruits.append(a)
a=input("과일을 입력하세요: \n")
fruits.append(a)
a=input("과일을 입력하세요: \n")
fruits.append(a)
a=input("과일을 입력하세요: \n")
fruits.append(a)
a=input("과일을 입력하세요: \n")
fruits.append(a)

print(f"{random.choice(fruits)}가 참 맛있죠!")
