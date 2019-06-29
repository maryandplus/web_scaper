#initial phase_ scrapping from web archive
# important NOTE! if you use a for loop use sleep.time() function 

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
url = "https://web.archive.org/web/xxxXXXXXXxxxxx"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.findAll('span' , class_="xxXXXxx")
content
