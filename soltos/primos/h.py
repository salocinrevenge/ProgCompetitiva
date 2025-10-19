from math import floor

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n in (0,1):
        return False
    limite = floor(n**0.5)+1
    for i in range(3,limite,2):
        if n % i == 0:
            return False
    return True


def main():

    number = int(input())
    if number <= 2:
        print(2)
        return
    if number %2 == 0:
        number -=1

    while not is_prime(number):
        number-=2

    print(number)

main()

"""
Se isso passar, essa é a maior mentira e chute q eu ja dei

"""