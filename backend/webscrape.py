import requests
import re
from bs4 import BeautifulSoup
# from pprint import *

from ai import *

# Webscrap contents from the url parameter
def scrape(url):
    # Send a request to get the page content
    response = requests.get(url)
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract all text from the page
    content = soup.get_text()
    format_content = trim(content)
    print(format_content)
    print(f'THE CONTENTS ARE : {verify(content,trim(content))}')
    # print(re.sub(' +',' ', content))

    # format_content = pprint.pformat(content)
    
    # print(format_content)
    
    return 0

# Website URL
url = "https://www.recipetineats.com/how-to-boil-eggs/"
scrape(url)