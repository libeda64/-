numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

q = numbers[:4]
w = numbers[5:]
legit = (q+w)

mean = sum(legit)/len(numbers)
numbers[4] = mean

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
