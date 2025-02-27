
#Задачка на треугольник
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не сущетсвует')
elif a != b and a != c and b != c:
    print('Разносторонний')
elif a ==b == c:
    print('Равносторонний')
else:
    print('Равнобедренный')

