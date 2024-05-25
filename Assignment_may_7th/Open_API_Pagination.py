# Imports
import requests
import json
import pandas as pd

baseurl  = "https://rickandmortyapi.com/api/"
endpoint = "character"

def main_request(baseurl , endpoint, x):
    response = requests.get(baseurl+endpoint+ f"/?page={x}")
    return response

response = main_request(baseurl , endpoint, 1)


def get_pages(response):
    pages = response.json()['info']['pages']
    return pages

print(get_pages(response=response))

# # Create a function returns all the name and number of episodes from that pages
main_list = []
def parse_page(response):
    for item in response.json()['results']:
        data_frame={}
        data_frame['name']=item['name']
        data_frame['episode']=item['episode']
        print(data_frame)
        main_list.append(data_frame)
    pd.DataFrame(main_list).to_csv('rickandmortyapi_character_info.csv', index=False)

# # Paginationto completed

for page in range(1,int(get_pages(response=response)+1)):
    print("Page number-----------",page)
    response = main_request(baseurl , endpoint, page)
    parse_page(response)


