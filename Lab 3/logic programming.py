from pyDatalog import pyDatalog

log = open("log.txt", 'w')

a_n = 999
d = 1  # difference of successive members

# first task
pyDatalog.create_terms('series_sum, N, Series_sum')

series_sum[0] = 0
series_sum[N] = N + series_sum[N - d]
log.write("Сумма ряда 0 - 999 999: " + str(series_sum[a_n] == Series_sum) + '\n')
