"""
contar palabras ofensivas en un archivo o una web
"""

from urllib import request
from urllib.error import URLError
lpo = ["coño", "bobo", "idiota", "estupido", "israel"]

def verify(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return("la url " + url + " no existe")
    else:
        aux = f.read()
        content = aux.split()
        bad_words = []
        counter = 0

        for l in lpo:
            for con in content:
                if l in con.decode():
                    bad_words.append(l)
        
        return bad_words
    
url = "https://www.abc.com.py/"

print("\n------------------------------------\n")
print(verify(url))