cifra = input("Цифра: ")
nameFile = input("файл: ")

if cifra.isdigit():
    count = 0
    with open(nameFile, 'r') as file:
        for line in file:
            for el in line:
                if el == cifra:
                    count += 1
    print(count)
else:
    print("Ошибка ввода")
