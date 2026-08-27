import random

import matplotlib.pyplot as plt
import numpy as np

chance_of_choice=0.5
choice_list = [5714, 2857, 1429]

fragment_list = [6501, 2984, 357, 114, 44]
fragment_occurence = [0]*18

for i in range(1000000):

    left = 9

    choice_random = random.randint(1, 20000)
    if choice_random > 10000:
        if choice_random <= 10000+choice_list[0]:
            left = 8
        elif choice_random <= 10000+choice_list[0]+choice_list[1]:
            left = 7
        else:
            left = 6

    outcome = []

    for j in range(left):
        fragment_random = random.randint(1,10000)

        total = 0
        for k in range(len(fragment_list)):
            total += fragment_list[k]
            if fragment_random <= total:
                outcome.append(k)
                break

    total_fragment = 0
    total_fragment += sum(outcome)

    if total_fragment > 17:
        total_fragment = 17
    elif total_fragment == 0:
        total_fragment = 1

    fragment_occurence[total_fragment] += 1


fragment_occurence = [m / 10000 for m in fragment_occurence]
print(fragment_occurence)


supercells_data = [0, 12.02, 14.03, 16.03, 20.04, 14.03, 10.02, 6.01, 2.2, 1.8, 1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2, 0.4]

x = np.array([i for i in range(18)])

y1 = np.array(fragment_occurence)
plt.bar(x+0.2, y1, 0.4)

y2 = np.array(supercells_data)
plt.bar(x-0.2, y2, 0.4)

plt.show()


# a = 0
# b = [0.5, 0.5*0.5714, 0.5*0.2857, 0.5*0.1429]
# for i in range(4):
#     print(8-i)
#     a += b[i]*(0.6501**(8-i))*0.2984*(9-i)+(0.6501**(9-i))
# print(a)
# test
# test pulling
