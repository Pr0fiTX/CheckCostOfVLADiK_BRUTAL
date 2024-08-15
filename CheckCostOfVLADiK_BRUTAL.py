import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

a = 1

def sooooooon():

    url = 'https://store.steampowered.com/app/1316680/VLADiK_BRUTAL/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        someText = soup.find('div', class_="discount_block game_purchase_discount")

        if someText:
            holdingText = someText.get('aria-label')
            print(holdingText)
        else:
            print('Элемент не найден.')
    else:
        print('Не удалось получить страницу, статус:', response.status_code)

while a == 1:
    sooooooon()
    print(datetime.now().strftime('%H:%M:%S'))
    time.sleep(3)