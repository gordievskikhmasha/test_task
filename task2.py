digits = tuple(map(int, input("Введите 6 цифр: ")))

if len(digits) == 6 and sum(digits[:3]) == sum(digits[3:]):
    print("Счастливый билет")
else:
    print("Несчастливый билет")