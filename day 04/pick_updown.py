#pick_updown


#유저한테 해당 범위를 지정 받습니다.
#n의 범위를 지정해주세요
#1~n 어떤 정수를 임의로 뽑히고
#총 1번 기회를 통해서 해당 숫자를 맞추기
#맞는다면 맞습니다! 축하드립니다!
#틀리면 틀렸습니다! 다시한번 맞춰보세요!

import random

a = int(input("n의 범위를 지정해주세요: \n"))
b = random.randint(1,a)
c = int(input("정수를 뽑아주세요 : \n"))
result = "맞습니다! 축하드립니다!" if b == c else "틀렸습니다!"
print(result)



