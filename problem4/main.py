def palindrome(input_string):
        reverse = input_string[::-1]
        return input_string == reverse
        return 'error response'


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False