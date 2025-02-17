from pymongo import MongoClient
client = MongoClient("client")
db = client.scrapy
collection= db.test_collection
doc=post={'author' :'Mike',
          

}
