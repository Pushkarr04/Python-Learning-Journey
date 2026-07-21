password = input("Enter your password : ")

uppercase = 0
lowercase = 0
digit = 0
special = 0
alphabet = 0

print("="*40)
print("PASSWORD SECURITY ANALYZER")
print("="*40)

print("\nPassword :", password)
print("Password Length :", len(password))



for char in password:

    if 'A' <= char <= 'Z':
        uppercase += 1
        alphabet += 1

    elif 'a' <= char <= 'z':
        lowercase += 1
        alphabet += 1

    elif '0' <= char <= '9':
        digit += 1

    elif char in "!@#$%&*":
        special += 1


print("\nSecurity checks:\n")



if len(password) >= 8:
    print("Length Check       : PASS")
else:
    print("Length Check       : FAIL")



if alphabet > 0:
    print("Alphabet Check     : PASS")
else:
    print("Alphabet Check     : FAIL")



if uppercase > 0:
    print("Uppercase Check    : PASS")
else:
    print("Uppercase Check    : FAIL")


if lowercase > 0:
    print("Lowercase Check    : PASS")
else:
    print("Lowercase Check    : FAIL")


if digit > 0:
    print("Digit Check        : PASS")
else:
    print("Digit Check        : FAIL")


if special > 0:
    print("Special Char Check : PASS")
else:
    print("Special Char Check : FAIL")


score = 0

if len(password) >= 8:
    score += 1

if alphabet > 0:
    score += 1

if uppercase > 0:
    score += 1

if lowercase > 0:
    score += 1

if digit > 0:
    score += 1

if special > 0:
    score += 1


print("\nSecurity Score :", score, "/6")


if score == 6:
    print("Password Strength : STRONG PASSWORD")

elif score >= 4:
    print("Password Strength : MEDIUM PASSWORD")

else:
    print("Password Strength : WEAK PASSWORD")


print("="*40)