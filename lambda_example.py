# Звичайна функція
def square(x):
    return x ** 2

# Лямбда-функція 
square_lambda = lambda x: x ** 2

numbers = [1, 2, 3, 4]

# Використання лямбди з map()
squares = list(map(lambda x: x ** 2, numbers))

# Фільтрація парних чисел
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Lyambda-vyrazy:")
print("Kvadraty:", squares)
print("Parni:", evens)