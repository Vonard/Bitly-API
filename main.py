import requests
import json
import os
from urllib.parse import urlparse, urlunparse
import argparse
from dotenv import load_dotenv



def shorten_link(token, link):
    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "long_url": link
    }
    response = requests.post(url, json=payload,headers=headers)
    response.raise_for_status()
    return response.json()["link"]

def count_clicks(token, link): 
    link = urlparse(link)
    link = f"{link.netloc}{link.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token, link):
    bitlink = urlparse(link)
    bitlink = f"{bitlink.netloc}{bitlink.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.ok
    

if __name__ == "__main__":
    load_dotenv()
    bitly_token = os.environ['BITLY_API']
    parser = argparse.ArgumentParser(description="Программа сокращает ссылки или позволяет посмотреть количество кликов по ссылке")
    parser.add_argument("url", help="Ссылка для выполнения программы.")
    args = parser.parse_args()
    try:
        if is_bitlink(bitly_token, args.url):
            print("Количество кликов по ссылке:", count_clicks(bitly_token, args.url))
        else:
            print('Битлинк:', shorten_link(bitly_token, args.url))
    except requests.exceptions.HTTPError:
        print("Ссылка введена неправильно!")

