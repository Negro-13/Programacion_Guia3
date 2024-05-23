import pyperclip
import requests
from bs4 import BeautifulSoup
##https://www.asambleanacional.gob.ec/es/contenido/transparencia-2021
url = ''
while True:
    burl = pyperclip.paste()
    if burl != url:
        url1 = requests.get(burl)
        if url1.status_code == 200:
            html = open('./Programacion_Guia3/Ejercicio 4/Web.html', 'wb')
            for chunk in url1.iter_content(100000):
                html.write(chunk)
            html.flush()
            url = burl
            print(f'La URL usada es: {burl}')
            html = open('./Programacion_Guia3/Ejercicio 4/Web.html', 'rb')
            soup = BeautifulSoup(html, 'html.parser')
            print('Las URL de los pdf encontrados son: ')
            for a in soup.find_all('a', href=True):
                if a['href'].endswith('.pdf'):
                    print(a['href'])
        else:
            print(f'La URL {burl} no es valida')