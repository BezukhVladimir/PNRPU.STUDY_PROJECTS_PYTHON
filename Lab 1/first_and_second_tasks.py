log = open("log.txt", 'w')

a = 0
a_n = 999999
n = 1000000
d = 1 # difference of successive members
series_sum = (a + a_n) * n / 2
log.write("Сумма ряда 0 - 999 999: " + str(series_sum))
