import requests
from bs4 import BeautifulSoup


main_url = "https://snapdeal.com/"


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'en-US,en;q=0.9',
    'Referer':'https://www.snapdeal.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

def send_request():
    response = requests.get(url=main_url)
    return response

response = send_request()

def get_product_urls(response):
    soup = BeautifulSoup(response.text,'html.parser')
    li = soup.find(True, string="Home & Kitchen").parent.parent
    a_tags = li.find_all('a',class_="rightMenuLink noHasTagWidth dp-widget-link")
    for tag in a_tags:
        product_url = tag.attrs['href']
        print(product_url)
        response_2 = requests.get(url=product_url,headers=headers)
        print(response_2)
        product_page = BeautifulSoup(response_2.text,'html.parser')
        for title in product_page.find_all("p",class_="product-title"):
            product_title = title.text
            print(product_title)
        

get_product_urls(response)

