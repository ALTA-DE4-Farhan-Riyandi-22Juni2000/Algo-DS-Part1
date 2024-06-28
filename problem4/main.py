import math

def generate_primes_grid(width, height, start):
    def prime_number(number):
        if number < 2:
            return False
        sqrt_ceiling = math.ceil(math.sqrt(number))
        for i in range(2, sqrt_ceiling + 1):
            if number % i == 0 and i != number:
                return False
        return True
    
    result = ""
    current_number = start
    while prime_number(current_number):
        current_number += 1
    for row in range(height):
        row_values = []
        for col in range(width):
            while not prime_number(current_number):
                current_number += 1
            row_values.append(current_number)
            current_number += 1
        result += " ".join(map(str, row_values)) + "\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """