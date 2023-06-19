# Web scrapper
# Author emailto:aleph_n@desarrollo.space
# ToDo: see README.md

import requests
from bs4 import BeautifulSoup
import random
import csv
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

# Generate random user agent
def generate_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        # Add more user agents as needed
    ]
    return random.choice(user_agents)

# Generate random browser size
def generate_random_screen_size():
    screen_sizes = [
        "1920x1080",
        "1366x768",
        "1440x900",
        # Add more screen sizes as needed
    ]
    return random.choice(screen_sizes)

# Generate random time zone
def generate_random_time_zone():
    time_zones = [
        "UTC",
        "America/New_York",
        "Europe/London",
        # Add more time zones as needed
    ]
    return random.choice(time_zones)

# Generate random operating system
def generate_random_os():
    operating_systems = [
        "Windows",
        "Mac",
        "Linux",
        # Add more operating systems as needed
    ]
    return random.choice(operating_systems)

# Generate random user information
def generate_random_user_info():
    fake = Faker()
    user_agent = generate_random_user_agent()
    browser_size = generate_random_screen_size()
    time_zone = generate_random_time_zone()
    operating_system = generate_random_os()

    user_info = {
        'user_agent': user_agent,
        'browser_size': browser_size,
        'time_zone': time_zone,
        'operating_system': operating_system,
        'name': fake.name(),
        'email': fake.email(),
        'phone_number': fake.phone_number()
    }
    return user_info

# Perform web crawling
def web_crawl(url):
    # Generate random user info
    user_info = generate_random_user_info()
    user_agent = user_info['user_agent']
    browser_size = user_info['browser_size']
    time_zone = user_info['time_zone']
    operating_system = user_info['operating_system']

    # Set up headless browser with Selenium
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument(f'window-size={browser_size}')
    chrome_options.add_argument(f'--lang=en')
    chrome_options.add_argument(f'--timezone={time_zone}')
    chrome_options.add_argument(f'--user-data-dir=profiles/{operating_system.lower()}')
    driver = webdriver.Chrome(options=chrome_options)

    # Make the request
    driver.get(url)

    # Extract data using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Extract desired data from the soup object
    rev_table = soup.find("table",attrs={"class","a-normal a-spacing-micro"})

    # Extract tagle data
    table_data = []
    for row in rev_table.find_all('tr'):
        row_data = []
        for cell in row.find_all(['th', 'td']):
            row_data.append(cell.text.strip())
        table_data.append(row_data)

    transposed_data = list(map(list, zip(*table_data)))

    # Set execution timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Apend tiemstamp to the filename
    filename = f"table_data_{timestamp}.csv"

    # Print the table data into a CSV file
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        print( transposed_data )
        writer.writerows(transposed_data)

    # Close the browser
    driver.quit()


# Define the URL you want to crawl
url = 'https://www.amazon.com.mx/Luuna-Colchón-Memory-Látex-Matrimonial/dp/B019YBYBSC'

# Call the web crawling function
if __name__ == "__main__":
    web_crawl(url)
