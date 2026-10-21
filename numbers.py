
import random

print("Числовая угадайка")

start = int(input("Введи начало диапазона: "))
end = int(input("Введи конец диапазона: "))

number = random.randint(start, end)  # Компьютер загадывает число

for attempt in range(1, 101):  # Не больше 100 попыток
    guess = int(input("Попробуй угадать: "))

    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print(f"Угадал! Попыток: {attempt}")
        break  # Завершаем цикл, если число угадано

else:
    print(f"Попытки закончились. Загаданное число: {number}")
