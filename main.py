start = int(input("Введіть початкове число діапазону: "))
end = int(input("Введіть кінцеве число діапазону: "))
for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
