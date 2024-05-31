import time

# Функция для тестирования производительности
def performance_test():
    start_time = time.time()
    # Добавьте здесь код для тестирования производительности
    end_time = time.time()
    duration = end_time - start_time
    return duration

# Запуск тестирования производительности
result = performance_test()
print(f"Тестирование производительности завершено за {result} секунд")
