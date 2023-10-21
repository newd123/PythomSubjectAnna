import time

age = int(input("Введіть свій вік:"))
if age<18:
    print("Допуск закрито")
else:
    print("Допуск відкрито")
    time.sleep(2)