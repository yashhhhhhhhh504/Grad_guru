import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
}
url = "https://collegedunia.com/study-abroad-universities"

lonky = []
finalinks = set()  

while True:

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    for link in links:
        lonky.append(str(link["href"]))

    for i in lonky:
        if i.count('/') == 3 and '?' not in i:
            finalinks.add(i)

    next_page = soup.select_one(".active + li a")
    if not next_page:
        break

    url = "https://collegedunia.com" + next_page["href"]

finalinks = list(finalinks)

file_path = "links.txt"

with open("links.txt", "w") as file:
    for link in finalinks:
        file.write(link + "\n")

print(f"Links have been written to links.txt")
