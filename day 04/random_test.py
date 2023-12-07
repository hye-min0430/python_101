import random

player = ['손흥민', '김민재','황희찬','이강인']
a = random.randint(0,3) #0~3에서 정수 하나 뽑기
b=random.choice(player) #리스트에서 하나 뽑기
random.shuffle(player)
c=random.uniform(1.5,2.5)
print(player[a])




