from random import randint

def roll_dice(n = 2):   # n=2 is default number, if there is no inputs when you call this function, the n use default number 2
    total = 0           # roll the dice, and return total number, duce number origanlly is 2
    for _ in range(n):
        total += randint(1,6)
    return total


def add(a=0, b=0, c=0):
    return a+b+c


def main():

    print(roll_dice(5))
    print(add(1,2,3))

if __name__ == '__main__':
    main()