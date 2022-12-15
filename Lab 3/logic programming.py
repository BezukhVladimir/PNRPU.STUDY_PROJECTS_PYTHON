from random import randint
from pyDatalog import pyDatalog

log = open("log.txt", 'w')

a_n = 999
d = 1  # difference of successive members

# first task
pyDatalog.create_terms('series_sum, N, Series_sum')

series_sum[0] = 0
series_sum[N] = N + series_sum[N - d]
log.write("Сумма ряда 0 - 999\n"
          + str(series_sum[a_n] == Series_sum)
          + "\n\n")

# second task
pyDatalog.create_terms('series_mean, Series_mean')

series_mean[N] = series_sum[N] / N
log.write("Среднее значение ряда\n"
          + str(series_mean[a_n] == Series_mean)
          + "\n\n")

# third task
pyDatalog.create_terms('rns, median, Median')

for i in range(a_n):
    rns[i] = randint(1, 10)
rns.sort()

median[N] = rns[N // 2] if a_n % 2 == 1\
    else (rns[(N / 2) - 1] + rns[N / 2]) / 2

log.write("Медиана ряда 999 целых случайных чисел от 1 до 10\n"
          + str(median[a_n] == Median)
          + "\n\n")
