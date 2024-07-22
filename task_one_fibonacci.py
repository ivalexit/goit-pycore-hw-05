def caching_fibonacci():
# Ініціалізація кешу
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
# Якщо значення вже кешоване, повертаємо його
        if n in cache:
            return cache[n]
# Обчислення (якщо немає в кеші) та збереження в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використання функції для обчислення чисел Фібоначчі
print(fib(10))  
print(fib(15))  

print(caching_fibonacci()(15))
print(caching_fibonacci()(10))