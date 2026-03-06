"""
contar palabras con un archivo o una web
"""

from urllib import request
from urllib.error import URLError

def word_count(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return("la url " + url + " no existe")
    else:
        content = f.read()
        return len(content.split())
    
url = "https://www.abc.com.py/"

print("\n------------------------------------\n")
print(word_count(url))