import pyperclip
import requests
from bs4 import BeautifulSoup

url = ''
while True:
    burl = pyperclip.paste()
    if burl != url:
        url1 = requests.get(burl)
        if url1.status_code == 200:
            html = open('./Programacion_Guia3/Ejercicio 2/Web.txt', 'wb')
            for chunk in url1.iter_content(100000):
                html.write(chunk)
            html.flush()
            url = burl
            print(f'La URL usada es: {burl}')
            html = open('./Programacion_Guia3/Ejercicio 2/Web.txt', 'rb')
            soup = BeautifulSoup(html, 'html.parser')
            print('Los parrafos encontrados son:')
            print(soup.find_all('p'))
        else:
            print(f'La URL {burl} no es valida')