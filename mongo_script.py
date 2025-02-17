from pymongo import MongoClient
client = MongoClient('mongodb+srv://lakshyakaushik:Lakshya12345678@cluster0.kllw6.mongodb.net/')
db = client.scrapy
collection= db.test_collection
doc=post={'author' :'Mike',
          

}