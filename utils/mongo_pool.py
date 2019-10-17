from pymongo import MongoClient
client = MongoClient("mongodb://root:root@106.13.222.216:27017/?authSource=admin")
#pymongo 内部维护了连接池, 所以不需要我们去 定义
# db = client["user"] #库

# collection = db["users"] #表

# collection.insert_one({'name':'zhangsan'}) #数据