import requests
from bs4 import BeautifulSoup

# Define the URL of the search results page
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all elements that contain article titles
    # The specific class names and tags might need to be adjusted based on the actual HTML structure
    titles = soup.find_all('a', class_='news_tit')
    
    # Extract and print the titles
    for title in titles:
        print(title.get('title'))
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
