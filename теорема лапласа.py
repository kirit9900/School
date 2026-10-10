import random
import matplotlib.pyplot as plt
import time
st = time.time()
one = []
two = []
k = False
for i in range(1001):
    onehandred = random.randint(1,100)
    one.append(onehandred)
while True:
    k = False
    for i in range(len(one)-1):
        if one[i] > one[i+1]:
            k = True
            p = one[i+1]
            one[i+1] = one[i]
            one[i] = p
    if not k:
        print(one)
        break
end = time.time()
print(end-st)






