import random

import matplotlib.pyplot as plt
import numpy as np

chance_of_choice=0.5
choice_list = [5714, 2857, 1429]

fragment_list = [6501, 2984, 357, 114, 44]
fragment_occurence = [0]*18

power_list = []
gadget_list = []
gear_list = []
star_power_list = []
hyper_list = []

iteration = 1000000

for i in range(iteration):

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

    #print(outcome)

    power_lvl = 1
    gadget = False
    gear = False
    star_power = False
    hyper = False
    for k in outcome:
        if k > 0:
            if k == 1:
                if power_lvl >= 11:
                    print("power overload 1")
                else:
                    power_lvl += 1

            elif k == 2:
                if power_lvl >= 10 and gear and gadget:
                    print("power overload 2")

                else:
                    exit = False
                    while not exit:
                        reward = random.randint(1,3)
                        if reward == 1 and power_lvl < 10:
                            power_lvl += 2
                            exit = True
                        elif reward == 2 and not gadget:
                            gadget = True
                            exit = True
                        elif reward == 3 and not gear:
                            gear = True
                            exit = True

            elif k == 3:
                if power_lvl >= 9 and star_power:
                    print("power_overload 3")
                else:
                    reward = random.randint(1,2)
                    if (reward == 1 and not star_power) or (reward == 2 and power_lvl >= 9):
                        star_power = True
                    else:
                        power_lvl += 3



            elif k == 4:
                if power_lvl >= 8 and hyper:
                    print("power_overload 4")
                else:
                    reward = random.randint(1,2)
                    if (reward == 1 and not hyper) or (reward == 2 and power_lvl >= 8):
                        hyper = True
                    else:
                        power_lvl += 4

    if power_lvl == 1:
        power_lvl == 2
    power_list.append(power_lvl)
    gadget_list.append(gadget)
    gear_list.append(gear)
    star_power_list.append(star_power)
    hyper_list.append(hyper)
        


    total_fragment = 0
    total_fragment += sum(outcome)
    if total_fragment > 17:
        total_fragment = 17
    elif total_fragment == 0:
        total_fragment = 1

    fragment_occurence[total_fragment] += 1

#Post loop

print("\n\n")
#print(power_list)
# print(gadget_list)
# print(gear_list)
# print(star_power_list)
# print(hyper_list)

print(sum(power_list)/iteration)

count = 0
for i in gadget_list:
    if i == True:
        count += 1
print("Gadget:", count/iteration)

count = 0
for i in gear_list:
    if i == True:
        count += 1
print("Gear:", count/iteration)

count = 0
for i in star_power_list:
    if i == True:
        count += 1
print("Star power:", count/iteration)

count = 0
for i in hyper_list:
    if i == True:
        count += 1
print("Hyper:", count/iteration)








fragment_occurence = [m / iteration * 100 for m in fragment_occurence]
print(fragment_occurence)


supercells_data = [0, 12.02, 14.03, 16.03, 20.04, 14.03, 10.02, 6.01, 2.2, 1.8, 1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2, 0.4]

x = np.array([i for i in range(18)])

y1 = np.array(fragment_occurence)
plt.bar(x+0.2, y1, 0.4)

y2 = np.array(supercells_data)
plt.bar(x-0.2, y2, 0.4)

#plt.show()


# a = 0
# b = [0.5, 0.5*0.5714, 0.5*0.2857, 0.5*0.1429]
# for i in range(4):
#     print(8-i)
#     a += b[i]*(0.6501**(8-i))*0.2984*(9-i)+(0.6501**(9-i))
# print(a)
# test
# test pulling
