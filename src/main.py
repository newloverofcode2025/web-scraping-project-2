import requests
from bs4 import BeautifulSoup
import json
import os

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the website
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
except requests.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the elements you want to scrape
# For example, let's scrape all the <a> tags
links = soup.find_all('a')

# Create a list to store the data
data = []

# Extract the text and href attributes from each link
for link in links:
    data.append({
        'text': link.get_text(),
        'href': link.get('href')
    })

# Ensure the data directory exists
output_dir = '../data'
os.makedirs(output_dir, exist_ok=True)

# Save the data to a JSON file
output_file = os.path.join(output_dir, 'output.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f'Scraping complete. Data saved to {output_file}')