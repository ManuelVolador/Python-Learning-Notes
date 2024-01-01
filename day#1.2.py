import random

random_num = random.randint(1,2)
random_num_2 = random.randint(1, 2)
print(random_num)
if random_num == 1:
    print("Vives")
else:
    print("Mueres")
    print(random_num_2)
    if random_num_2 == 1:
        print("Vives otra vez")
    else:
        print("mal")