import requests
from bs4 import BeautifulSoup
from googletrans import Translator
translator = Translator()


main_url = "https://www.kotsovolos.gr/household-appliances/fridges/fridge-freezers"

url = "https://www.kotsovolos.gr/api/ext/getProductsByCategory?params=pageNumber%3D1%26pageSize%3D36%26catalogId%3D10551%26langId%3D-24%26orderBy%3D5&catId=35822&storeId=10151&isCPage=false"


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'en-US,en;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
for entry in response.json()['catalogEntryView']:
    print('Original product url--------',entry['UserData'][0]['seo_url'])
    if "household-appliances/fridges/fridge-freezers/" in entry['UserData'][0]['seo_url']:
        product_url = "https://www.kotsovolos.gr/"+entry['UserData'][0]['seo_url']
    else:
        product_url = "https://www.kotsovolos.gr/household-appliances/fridges/fridge-freezers/"+entry['UserData'][0]['seo_url']
    print("Product_url------------",product_url)
    response_2 = requests.get(url=product_url,headers=headers)
    #print(response_2.text)
    soup = BeautifulSoup(response_2.text,"html.parser")
    product_name = soup.find("h2",class_="MuiTypography-root sc-5006bef8-0 khVZHy MuiTypography-h2").text
    print(translator.translate(product_name,dest='en').text)
