# import sqlite3

# conn = sqlite3.connect("laptops_info.db")

# curr = conn.cursor()

# #Create table
# # curr.execute('''
# #     create table aoneplus_laptops_info(
# #     product_name text,product_img_url text,product_price int)
# # ''')

# curr.execute('''
#     insert into aoneplus_laptops_info values('scrapy is awson','zyte','webscraping')
# ''')

# conn.commit()
# conn.close()