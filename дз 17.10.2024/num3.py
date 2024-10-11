nameFile = input("Файл: ")
file = open(nameFile)
k = 0
for line in file:
    k += line.count("ab")
print(k)
