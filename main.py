import math

#Функция для вычисления гипотенузы равнобедренного треугольника
def calculate_hypotenuse(a):
    hypotenuse = a * math.sqrt(2)
    return hypotenuse

#Запрос длины катета у пользователя
a = float(input("Введите длину катета равнобедренного треугольника: "))

#Вычисление гипотенузы
hypotenuse = calculate_hypotenuse(a)

#Вывод результата
print(f"Гипотенуза равнобедренного треугольника с катетом длиной {a} равна {hypotenuse: .2f}")
