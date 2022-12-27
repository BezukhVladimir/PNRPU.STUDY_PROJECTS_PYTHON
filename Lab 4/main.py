import requests
from bs4 import BeautifulSoup
from sklearn import datasets
from reduce import reduce

log = open("log.txt", 'w')

items = [1, 2, 3, 4, 5]
log.write(f"Метод reduce\n"
          f"{reduce(lambda x, y: x + y, items)}\n"
          f"\n")
log.write(f"Метод map\n"
          f"{list(map(lambda x: x ** 2, items))}\n")

url = "https://perm.kinoafisha.info/cinema/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
all_cinemas_names = soup.find_all(class_="cinemaList_name")
cinemas = []
for item in all_cinemas_names:
    item_name = item.text
    cinemas.append(item_name)
log.write(f"\nМетод reduce\n"
          f"{reduce(lambda x, y: '{0}{1}'.format(x, y), cinemas)}\n"
          f"\n")
log.write(f"Метод map\n"
          f"{list(map(lambda x: x * 2, cinemas))}\n")

wine = datasets.load_wine()
names_list = list(wine.items())
log.write(f"\nМетод reduce\n"
          f"{reduce(lambda x, y: '{0}{1}'.format(x, y), names_list)}\n"
          f"\n")
log.write(f"Метод map\n"
          f"{list(map(lambda x: x * 2, names_list))}")

log.close()
