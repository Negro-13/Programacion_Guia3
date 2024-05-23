import pyperclip
import requests
from bs4 import BeautifulSoup

url = ''
while True:
    burl = pyperclip.paste()
    if burl != url:
        url1 = requests.get(burl)
        if url1.status_code == 200:
            html = open('./Programacion_Guia3/Ejercicio 3/Web.html', 'wb')
            for chunk in url1.iter_content(100000):
                html.write(chunk)
            html.flush()
            url = burl
            print(f'La URL usada es: {burl}')
            html = open('./Programacion_Guia3/Ejercicio 3/Web.html', 'rb')
            soup = BeautifulSoup(html, 'html.parser')
            print('los links que llevan a otras paginas son:')
            for a in soup.find_all('a', href=True):
                if a['href'].startswith('http'):
                    print(a['href'])
            print('Si decea ver el contenido de alguno de estas URL, realize Ctrl + c al que usted requiera')
        else:
            print(f'La URL {burl} no es valida')