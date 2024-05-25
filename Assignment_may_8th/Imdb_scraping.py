import requests, openpyxl
from bs4 import BeautifulSoup

# Creating excel file 

excel = openpyxl.Workbook()
print(excel.sheetnames) ### Nmae of sheet
sheet = excel.active
sheet.append(['Movie Name' , 'Movie Rank' , 'Movie Year'])
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'


try: 
    headers = {'user-agent' :USER_AGENT }
    source = requests.get("https://www.imdb.com/chart/top/", headers=headers)
    # print(source.text) 
    print(source.status_code)  ## status code
    # print(source.raise_for_status)    ## raise to get an alert for incorrect urls

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base").find_all('li')
    result = []
    for movie in movies:
        second_div = movie.select_one('div:nth-of-type(2)')
        second_div.find('h3').text
        #name = movie.find('div' , class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text
        #rank = movie.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
        # rank.attrs['aria-label']
        #year = movie.find('span', class_="sc-b189961a-8 kLaxqf cli-title-metadata-item").text
        #result.append((name,rank.attrs['aria-label'],year))
        #print(result)
        #sheet.append([name,rank.attrs['aria-label'],year])
        break

except Exception as e:
    print(e) 

#excel.save('IMDB_MoviewRating.xlsx')

