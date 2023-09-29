def is_prime(N):
    # your code here
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

def full_prima(N):
    if N <= 1:
        return False
    number_str = str(N)
    for digit in number_str:
        if not is_prime(int(digit)):
            return False 
    return True 
    return ''

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True