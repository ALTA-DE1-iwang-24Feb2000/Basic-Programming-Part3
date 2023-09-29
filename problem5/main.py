def pangkat(base, pangkat):
    # your code here
    hasil = 1
    for i in range (0, pangkat):
        hasil *= base
    return hasil
    return 'error response'


if __name__ == '__main__':
    print(pangkat(2, 3)) # 8
    print(pangkat(5, 3)) # 125
    print(pangkat(10, 2)) # 100
    print(pangkat(2, 5)) # 32
    print(pangkat(7, 3)) # 343