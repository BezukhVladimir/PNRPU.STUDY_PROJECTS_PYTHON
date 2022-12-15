from math import prod
from random import randint
from statistics import median

log = open("log.txt", 'w')

a = 0
a_n = 999999
n = 1000000
d = 1  # difference of successive members

# first task
series_sum = (a + a_n) * n / 2
log.write(f"Сумма ряда 0 - 999 999:\n"
          f"{series_sum}\n"
          f"\n")

# second task
series_mean = series_sum / n
log.write(f"Среднее значение ряда:\n"
          f"{series_mean}\n"
          f"\n")

# third task
random_number_series = []
for i in range(1000000):
    random_number_series.append(randint(1, 10))
log.write(f"Медиана ряда 1 000 000 целых случайных чисел от 1 до 10:\n"
          f"{median(random_number_series)}\n"
          f"\n")

# fourth task
log.write(f"Произведение ряда 1 000 000 целых случайных чисел от 1 до 10:\n"
          f"{prod(random_number_series)}")
