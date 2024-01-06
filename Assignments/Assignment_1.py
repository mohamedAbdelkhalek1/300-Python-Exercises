"""
Build a command-line application that allows users to search for and download images from the internet using Python libraries
    such as Requests, BeautifulSoup, and Pillow.
"""
import requests
from bs4 import BeautifulSoup
from PIL import Image

def search_and_download_images(query, num_images):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img', limit=num_images)
    
    for i, img_element in enumerate(image_elements):
        image_url = img_element['src']
        response = requests.get(image_url)
        response.raise_for_status()
        
        with open(f"image_{i}.jpg", "wb") as f:
            f.write(response.content)
        
        # Optional: Resizing the downloaded images
        image = Image.open(f"image_{i}.jpg")
        image = image.resize((256, 256))
        image.save(f"image_{i}.jpg")

# Example usage:
search_and_download_images("cats", 5)