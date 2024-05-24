import requests
import pandas as pd

url = "https://www.brewersassociation.org/wp-content/themes/ba2019/json-store/breweries/breweries.json?nocache=1716527348243"

response = requests.get(url=url)
print(type(response.json()))

data_frame =[]
for company in response.json():
    company_details = {}
    company_details['Name']=company['Name']
    company_details['Phone']=company['Phone']
    company_details['BillingAddress']=company['BillingAddress']
    print(company_details)
    data_frame.append(company_details)

pd.DataFrame(data_frame).to_csv('breweries.csv', index=False)