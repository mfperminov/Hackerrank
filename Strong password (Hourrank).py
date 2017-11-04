import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    num=low=up=sp=0
    for i in range(n):
        if (password[i] in numbers):
            num=1
        if (password[i] in lower_case):
            low=1
        if (password[i] in upper_case):
            up=1
        if (password[i] in special_characters):
            sp=1
    missing=4-num-low-up-sp
    if n<6:
        if missing>(6-n):
            return missing
        else:
            return (6-n)
    else:
        return missing
if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
