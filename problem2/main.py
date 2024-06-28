import math

def primeX(x):
    if x <= 0:
        return None

    count = 0
    number = 2

    while count < x:
        prime_number = True
        sqrt_ceiling = math.ceil(math.sqrt(number))

        for i in range(2, sqrt_ceiling + 1):
            if number % i == 0 and i != number:
                prime_number = False
                break

        if prime_number:
            count += 1

        if count == x:
            return number

        number += 1

    return None


if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29