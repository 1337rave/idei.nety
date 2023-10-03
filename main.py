start = int(input("Введіть початкове число діапазону: "))
end = int(input("Введіть кінцеве число діапазону: "))
print("Всі числа в діапазоні:")
for number in range(start, end + 1):
    print(number, end=' ')
print()
print("Всі числа в діапазоні в спадному порядку:")
for number in range(end, start - 1, -1):
    print(number, end=' ')
print()
print("Числа, кратні 7:")
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number, end=' ')
print()
count_multiples_of_5 = 0
for number in range(start, end + 1):
    if number % 5 == 0:
        count_multiples_of_5 += 1

print("Кількість чисел, кратних 5:", count_multiples_of_5)
