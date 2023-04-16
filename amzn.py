import requests
from requests_html import HTMLSession
import pandas as pd

url = "https://www.amazon.in/s?k=iphone+13&crid=D8X8TVNOI5AX&sprefix=iphone%2Caps%2C528&ref=nb_sb_ss_ts-doa-p_1_6"

try:
    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout=10000)

    f = open("index.html", "a")
    f.write(response.html.html)
    f.close()

    item_name = []
    item_price = []

    for index in range(0, 20):
        for item in response.html.xpath(
                f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{index}]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'):
            item_name.append(item.text)

        for item in response.html.xpath(
                f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{index}]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]'):
            item_price.append(item.text)

        for item in response.html.xpath(
                f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{index}]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/a/span[1]/span[2]/span[2]'):
            item_price.append(item.text)

    dic = {"item_name": item_name, "item_price": item_price}
    df = pd.DataFrame(dic)

    print(df)
    print(len(item_name), len(item_price))

except requests.exceptions.RequestException as e:
    print(e)
