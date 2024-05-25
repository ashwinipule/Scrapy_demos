import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import pandas as pd
translator = Translator()


#main_url = "https://www.kotsovolos.gr/household-appliances/fridges/fridge-freezers"

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'en-US,en;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def get_page_count():
    url = "https://www.kotsovolos.gr/api/ext/getProductsByCategory?params=pageNumber%3D1%26pageSize%3D36%26catalogId%3D10551%26langId%3D-24%26orderBy%3D5&catId=35822&storeId=10151&isCPage=false"
    response = requests.get(url=url,headers=headers)
    total_products = response.json()['recordSetTotal']
    products_per_page = response.json()['recordSetCount']
    page_count = round(int(total_products)/int(products_per_page))
    return page_count

def get_product_details():

    main_list = []

    page_count = get_page_count()

    for page in range(1,page_count+1):

        print("Page number----------",page)

        url = "https://www.kotsovolos.gr/api/ext/getProductsByCategory?params=pageNumber%3D"+str(page)+"%26pageSize%3D36%26catalogId%3D10551%26langId%3D-24%26orderBy%3D5&catId=35822&storeId=10151&isCPage=false"

        response = requests.get(url=url,headers=headers)
        
        for entry in response.json()['catalogEntryView']:

            data_frame = {}

            print('Original product url--------',entry['UserData'][0]['seo_url'])
            
            product_name_greek = entry['name']

            product_name = translator.translate(product_name_greek,dest='en').text

            product_short_desc_greek = entry['shortDescription']

            product_short_desc = translator.translate(product_short_desc_greek,dest='en').text

            product_price = entry['price_EUR']

            if "household-appliances/fridges/fridge-freezers/" in entry['UserData'][0]['seo_url']:
                product_url = "https://www.kotsovolos.gr/"+entry['UserData'][0]['seo_url']
            else:
                product_url = "https://www.kotsovolos.gr/household-appliances/fridges/fridge-freezers/"+entry['UserData'][0]['seo_url']
            
            print("Product_url------------",product_url)

            # response_2 = requests.get(url=product_url,headers=headers)
            # #print(response_2.text)
            # soup = BeautifulSoup(response_2.text,"html.parser")
            # product_name_greek = soup.find("h2",class_="MuiTypography-root sc-5006bef8-0 khVZHy MuiTypography-h2").text
            
            data_frame['product_url']=product_url
            data_frame['product_name']=product_name
            data_frame['product_price']=product_price
            data_frame['product_short_desc']=product_short_desc

            print('product_details----------',data_frame)

            main_list.append(data_frame)

    pd.DataFrame(main_list).to_csv('kotsovolos.csv', index=False)

get_product_details()
