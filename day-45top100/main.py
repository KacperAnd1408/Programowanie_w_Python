import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL).text
soup = BeautifulSoup(response, 'html.parser')


film_titles = soup.find_all(name='h3', class_='title')
# print(film_titles)

list_titles = []

for title in film_titles:
    film = title.getText()
    list_titles.append(film)

list_titles.reverse()
n = len(film_titles)

with open("movies.txt", 'w', encoding="utf-8") as file:
    for i in range(n):
        if 'â' in list_titles[i]:
            list_titles[i].replace("â", "-")

        file.write(f"{list_titles[i]}\n")







