from random import randint
from pyDatalog import pyDatalog

log = open("log.txt", 'w')

a_n = 999
d = 1  # difference of successive members

# first task
pyDatalog.create_terms('series_sum, N, Series_sum')

series_sum[0] = 0
series_sum[N] = N + series_sum[N - d]

log.write(f"Сумма ряда 0 - 999\n"
          f"{series_sum[a_n] == Series_sum}\n"
          f"\n")

# second task
pyDatalog.create_terms('series_mean, Series_mean')

series_mean[N] = series_sum[N] / N

log.write(f"Среднее значение ряда\n"
          f"{(series_mean[a_n] == Series_mean)}\n"
          f"\n")

# third task
pyDatalog.create_terms('rns, median, Median')

for i in range(a_n):
    rns[i] = randint(1, 10)
rns.sort()

median[N] = rns[N // 2] if a_n % 2 == 1\
    else (rns[(N / 2) - 1] + rns[N / 2]) / 2

log.write(f"Медиана ряда 999 целых случайных чисел от 1 до 10\n"
          f"{(median[a_n] == Median)}\n"
          f"\n")

# fourth task
pyDatalog.create_terms('prod, Prod')

prod[1] = rns[0]
prod[N] = rns[N - 1] * prod[N - 1]

log.write(f"Произведение ряда 999 целых случайных чисел от 1 до 10:\n"
          f"{(prod[a_n] == Prod)}")

log.close()
