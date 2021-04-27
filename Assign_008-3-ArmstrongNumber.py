number = input("Please enter a positive integer number: ")
power = len(number)
result = 0
if number.startswith("-") or "." in number or "," in number or (not number.isdigit()):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in number:
        result += int(i) ** power
    if int(number) == result:
        print(f'{number} is an Armstrong number')
    else:
        print(f'{number} is not an Armstrong number')
