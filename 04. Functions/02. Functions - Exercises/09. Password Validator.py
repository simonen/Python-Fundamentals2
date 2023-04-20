def pass_validator(password_f, valid_chars_f):
    digits_count = 0
    valid = 1
    if len(password_f) not in range(6, 11):
        valid = 0
        print("Password must be between 6 and 10 characters")
    if any(i not in valid_chars_f for i in password_f):
        valid = 0
        print("Password must consist only of letters and digits")
    digits_count = len([x for x in password_f if ord(x) in range(48, 58)])
    if digits_count < 2:
        valid = 0
        print("Password must have at least 2 digits")
    if valid == 1:
        print("Password is valid")


password = list(input())

digits = list(map(ord, range(48, 58)))
uppercase = list(map(ord, range(65, 91)))
lowercase = list(map(ord, range(97, 123)))
valid_chars = digits + uppercase + lowercase

pass_validator(password, valid_chars)
