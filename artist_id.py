import requests, re
from bs4 import BeautifulSoup


def get_id(val):    
    url = ("https://www.google.com/search?q="+val+"spotify")
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser') 
    url = []
    for link in soup.find_all('a'):
        a = link.get('href')
        if a.startswith('/url?q=https://open.spotify.com/artist/'):
            url.append(a)
            
    
    data = url[0]
    data = data[7:61]
    md = data.split('/')
    return md[-1]



artist = input('Enter the artist name: ')
x = get_id(artist)
print(x)

