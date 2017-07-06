# Pythone v3.6

import requests

#--------------------------------------------------#

def get_web_page(url):
    request = requests.get(url)

    if request.status_code != 200:
        print("Invalid URL: ", request.url)
        return None
    else:
        return request.text

#--------------------------------------------------#

url = "http://8comic.se/103903/"
page = get_web_page(url)

print(page)
