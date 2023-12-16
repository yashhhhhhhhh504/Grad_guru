import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = "https://collegedunia.com/uk/university/865-university-of-oxford-oxford#showless"

# Define the user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the data
table = soup.find("table", {"class": "jsx-2775229226 table-common"})

# Extract data from the table
for row in table.find("tbody").find_all("tr"):
    program = row.find("a", {"class": "jsx-2775229226 d-block hover-underline"}).text
    deadline = row.find("span", {"class": "text-capitalize"}).text
    fees = row.find("span", {"class": "fee-total"}).text
    scores = [item.text for item in row.find("ul", {"class": "list-unstyled"}).find_all("span", {"class": "text-title font-weight-medium"})]

    print("Program:", program)
    print("Deadline:", deadline)
    print("Fees:", fees)
    print("Scores:", ", ".join(scores))
    print("\n")
