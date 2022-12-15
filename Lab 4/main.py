from reduce import reduce

log = open("log.txt", 'w')

items = [1, 2, 3, 4, 5]
log.write(f"Метод reduce\n"
          f"{reduce(lambda x, y: x + y, items)}\n"
          f"\n")
log.write(f"Метод map\n"
          f"{list(map(lambda x: x ** 2, items))}")
