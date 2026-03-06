import random

def add(a, b):
    return a + b

if name == "main":
    number = random.randint(0, 1000)
    guess = -1
    attempts = 0

    print("Гра: Вгадай число від 0 до 1000")

    while guess != number:
        guess = int(input("Введіть число: "))
        attempts += 1

        if guess < number:
            print("Загадане число більше")
        elif guess > number:
            print("Загадане число менше")
        else:
            print("Вітаю! Ви вгадали число.")
            print("Кількість спроб:", attempts)