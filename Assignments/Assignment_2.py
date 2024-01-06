"""
Create a web scraping tool that extracts data from a website and saves it to a CSV file using Python libraries 
    such as Requests, BeautifulSoup, and Pandas.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save_to_csv(url, csv_file):
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data from the website using BeautifulSoup
    
    # Example: Extracting headlines from a news website
    headlines = []
    headline_elements = soup.find_all('h2', class_='headline')
    for headline_element in headline_elements:
        headlines.append(headline_element.text)
    
    # Save the extracted data to a CSV file using Pandas
    df = pd.DataFrame({'Headline': headlines})
    df.to_csv(csv_file, index=False)

# Example usage:
scrape_and_save_to_csv("https://example.com/news", "news_headlines.csv")