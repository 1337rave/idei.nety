start = int(input("Введіть початкове число діапазону: "))
end = int(input("Введіть кінцеве число діапазону: "))
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)
