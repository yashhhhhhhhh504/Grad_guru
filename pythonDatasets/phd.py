import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.educations.com/search/doctorate-phd?page="
TOTAL_PAGES = 500

data = []

for page in range(1, TOTAL_PAGES + 1):
    URL = BASE_URL + str(page)
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    programs = soup.find_all('div', class_='emg-serp__row emg-serp__row-has-compare')

    for program in programs:
        program_name = program.find('h4', class_='emg-serp-item__title-text').text.strip()
        university_name = program.find('div', class_='emg-serp-item__subtitle').text.strip()
        location = program.find('li', class_='emg-serp-item__flag emg-serp-item__flag-place emg-serp-item__flag-1').text.strip()
        data.append([program_name, university_name, location])

with open('universities.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Program Name", "University Name", "Location"])  
    writer.writerows(data)
