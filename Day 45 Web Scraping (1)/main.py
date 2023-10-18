from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')
list = [item for item in soup.find_all(name="h3", class_="title")]
movies_list = [movie.getText() for movie in list]
movies_list.reverse()

with open("topmovies.txt", "w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
    file.close()

# response = requests.get(url="https://news.ycombinator.com/")
# soup = BeautifulSoup(response.text, "html.parser")
# titles = soup.find_all(name="span", class_="titleline")
# points_data = soup.find_all(name="span", class_="score")
# points = [each.getText() for each in points_data]
#
# scores = [int(letter) for each in points for letter in each.split() if letter.isdigit()]
# max_score = max(scores)
# index = scores.index(max_score)
#
# print(titles[index].getText())
# print(titles[index].a.get("href"))
# print(f"Points: {max_score}")

# soup = BeautifulSoup(contents, 'html.parser')
# anchor_tags = soup.find(name="h3", class_="heading")
# name = soup.select_one("p a")
# company_url = soup.select_one(selector="p a")
# print(anchor_tags.getText())
# print(name)
# print(company_url)

