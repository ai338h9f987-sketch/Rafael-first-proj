import time


def measure_time(func):
    start = time.time()
    result = func()
    end = time.time()
    return result, end - start


def slow_function():
    time.sleep(1)
    return "Готово"


# Тест
result, work_time = measure_time(slow_function)

assert result == "Готово"
assert work_time >= 1

print("Результат:", result)
print("Время работы:", work_time)
print("Тест прошёл успешно")