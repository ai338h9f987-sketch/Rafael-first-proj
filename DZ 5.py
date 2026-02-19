
import colorama
from colorama import Fore, Back, Style

# Смотрим, что есть внутри модуля
print("Что есть в colorama:")
print(dir(colorama))

print("\nЧто есть в Fore (цвет текста):")
print(dir(Fore))

print("\nЧто есть в Back (цвет фона):")
print(dir(Back))

print("\nЧто есть в Style (стиль текста):")
print(dir(Style))

# Включаем работу библиотеки
colorama.init(autoreset=True)

print("\nПримеры работы:\n")

# Цвет текста
print(Fore.RED + "Красный текст")
print(Fore.GREEN + "Зелёный текст")
print(Fore.BLUE + "Синий текст")

# Цвет фона
print(Back.YELLOW + "Жёлтый фон")
print(Back.CYAN + "Голубой фон")

# Стиль текста
print(Style.BRIGHT + "Яркий текст")
print(Style.DIM + "Тусклый текст")

# Всё вместе
print(Fore.WHITE + Back.RED + Style.BRIGHT + "Комбинированный текст")

# Сброс цвета вручную
print(Fore.RED + "Красный текст" + Style.RESET_ALL)
print("Обычный текст")
