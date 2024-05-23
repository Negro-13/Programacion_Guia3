import pyperclip
import requests

url = ''
while True:
    burl = pyperclip.paste()
    if burl != url:
        url1 = requests.get(burl)
        if url1.status_code == 200:
            html = open('./Programacion_Guia3/Ejercicio 1/Web.html', 'wb')
            for chunk in url1.iter_content(100000):
                html.write(chunk)
            url = burl
            print(f'La URL usada es: {burl}')
        else:
            print(f'La URL {burl} no es valida')
