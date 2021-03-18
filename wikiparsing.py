"""
Парсим список имен всех животных с википедии

еще не доделанный вариант кода!!!

добавит проверку на окончание ые е
недостаток по животным с некоторых букв


"""

from bs4 import BeautifulSoup
import requests

url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8' \
      '%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=0 '
main = []
while True:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        hive = soup.find(name="div", attrs={"class": "mw-category"}).ul
        for a in hive.find_all("a"):
            main.append(str(a.attrs["title"]))

        href = soup.find(name="a",
                         attrs={"title": "Категория:Животные по алфавиту"},
                         string=["Следующая страница"]).attrs["href"]

        url = f"https://ru.wikipedia.org{href}"
        print(url)
    except Exception as exc:
        print(exc.args)
        break

rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# eng = "abcdefghijklmnopqrstuvwxyz"
dict_names = {}
for letter in rus:
    let = []
    for name in main:
        if name.lower().startswith(letter):
            let.append(name)
        else:
            dict_names[letter] = len(let)

print(dict_names)
