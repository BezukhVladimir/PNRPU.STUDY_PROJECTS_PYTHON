from pyDatalog import pyDatalog

log = open("log.txt", 'w')

a_n = 999
d = 1  # difference of successive members

# first task
pyDatalog.create_terms('series_sum, N, Series_sum')

series_sum[0] = 0
series_sum[N] = N + series_sum[N - d]
log.write("Сумма ряда 0 - 999\n" + str(series_sum[a_n] == Series_sum) + "\n\n")

# second task
pyDatalog.create_terms('series_mean, Series_mean')

series_mean[N] = series_sum[N] / N
log.write("Среднее значение ряда\n" + str(series_mean[999] == Series_mean) + "\n\n")
