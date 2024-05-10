import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/static/computers/tablets"
def find_page_count():
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text,"html.parser")
    page_list = soup.find("ul",class_="pagination").find_all("li",class_="page-item")
    for li in page_list[1:5]:
        scrap_product_details(li)

def scrap_product_details(li):
    response = requests.get(url=url+"?page="+li.text)
    soup = BeautifulSoup(response.text,"html.parser")
    all_product_div = soup.find_all("div",class_="card thumbnail")
    product_details = {}
    for product in all_product_div:
        title = product.find('a',class_="title").text
        description = product.find('p',class_="description card-text").text
        price = product.find('h4',class_="price float-end card-title pull-right").text
        review = product.find('p',class_="review-count float-end").text
        product_details['title']=title
        product_details["description"]=description
        product_details['price']=price
        product_details["review"]=review
        print(product_details)
find_page_count()


