import threading

# Функция, которая будет выполняться в каждом потоке
def worker(num):
    print(f"Поток {num} начал работу")
    # Добавьте здесь код для тестирования функциональности многопоточности
    print(f"Поток {num} закончил работу")

# Создание и запуск потоков
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

print("Все потоки завершили работу")
