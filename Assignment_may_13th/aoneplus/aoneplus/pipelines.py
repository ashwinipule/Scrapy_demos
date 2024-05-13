# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


#This class contains logic to save data to sqlite3 db
class AoneplusPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("aoneplus.db")
        self.curr = self.connection.cursor()

    def create_table(self):
        #Create table
        self.curr.execute('''drop table if exists laptops_info''')
        self.curr.execute('''
            create table laptops_info(
            product_name text,product_img_url text,product_price int)
        ''')

    def store_data(self,item):
        self.curr.execute('''
        insert into laptops_info values(?,?,?)''',(", ".join(item['product_name']),
        item['product_img_url'][0],item['product_price']))
        self.connection.commit()

    def process_item(self, item, spider):
        #logic to save
        self.store_data(item)
        return item

    def close_spide(self):
        self.curr.close()
        self.connection.close()
