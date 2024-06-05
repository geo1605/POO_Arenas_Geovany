import random
conjunto1 = {1}
conjunto2 = {2}
conjunto3 = {3}


for i in range(0,10):
    conjunto1.add(random.randint(0,20))
    conjunto2.add(random.randint(0,20))
    conjunto3.add(random.randint(0,20))

conjuntoT = conjunto1 | conjunto2 | conjunto3
par = {num for num in conjuntoT
if num % 2 == 0}

print(conjuntoT, par)