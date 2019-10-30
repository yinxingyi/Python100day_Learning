# #-------------------------------------------------
# #Narcissistic Number
from math import pow, sqrt
from random import randint

def find_nar_number(range_num):
    for i in range(100, range_num):
        if pow((i//100),3)+pow(((i%100)//10),3)+pow((i%10),3) == i:
            print('%d is a Narcissistic number' %i)

# ---------------------------------------------------
# Find Perfect number
def find_perfect_number (range_num):
    for i in range (1,range_num):
        temp = 0
        for j in range(1, i):
            if i % j == 0:
                temp = temp + j
        if temp == i:
            print('%d is a perfect number' %i)

# ----------------------------------------------------------
#$100 for 100 chicken

def chicken():
    for num_cock in range(0,20):
        for num_hen in range(0,33):
            num_chick = 100 - num_cock - num_hen
            if 5 * num_cock + 3 * num_hen + num_chick / 3 == 100:
                print('cock: %d pcs, hen: %d pcs, check: %d pcs' %(num_cock,num_hen,num_chick))

# ------------------------------------------------------------
# Fibonacci Sequence
def find_fibon_number(range_num):
    for i in range(1,range_num):
        fibon_num = 1 / sqrt(5) * ((((1+sqrt(5))/2)**i)-(((1-sqrt(5))/2)**i))
        print(int(fibon_num))

# ---------------------------------------------------------------
# Craps
def craps():

    money = 1000

    while money > 0:
        print('you have $%d in your account' %money)
        go_on = False
        while True:
            debt = int(input('please bet:'))
            if 0 < debt < money:
                break
            else:
                print("you don't have that much money")

        round_1 = randint(1,6) + randint(1,6)
        print("round 1 craps are %d" %round_1)
        if round_1 == 7 or round_1 == 11:
            print('you win')
            money = money + debt
        elif round_1 == 2 or round_1 == 3 or round_1 == 12:
            print('you lose')
            money = money - debt
        else:
            go_on = True

        while go_on:
            round_2 = randint(1,6) + randint(1,6)
            print('round 2 craps are %d' %round_2)
            if round_2==7:
                print('you lose')
                money = money-debt
                go_on = False
            elif round_2 == round_1:
                print(' you win')
                money = money + debt
                go_on = False
    print('you lose all money')


# --------------------------------------------------------
# Main
def main():
    craps()

# -----------------------------------------------------------
if __name__== '__main__':
    main()



