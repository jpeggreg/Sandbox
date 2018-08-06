"""Greg Taylor"""

MINIMUM_LENGTH = 6

password = input("Enter a password with at least {} characters ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    password = input("Enter a password with at least {} characters ".format(MINIMUM_LENGTH))

print('*' * len(password))