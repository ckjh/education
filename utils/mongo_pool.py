from pymongo import MongoClient
client = MongoClient("mongodb://root:root@106.13.222.216:27017/?authSource=admin")
#pymongo 内部维护了连接池, 所以不需要我们去 定义
# db = client["user"] #库

# collection = db["users"] #表

# collection.insert_one({'name':'zhangsan'}) #数据


#<-------------------------------自增函数--------------------------------------->
#创建dbdb数据库
db =client['dbdb']

#创建username_id集合
username_id = db['username_id']

#自增函数(自增函数需要优先执行后,在执行数据添加)
def getNextValue(user_Name):
    ret = username_id.find_and_modify({"_id": user_Name}, {"$inc": {"sequence_value": 1}},  new=True)
    new = ret["sequence_value"]
    return new

if __name__=='__main__':
    #插入username_id
    username_id.insert_one(({'_id': 'name', 'sequence_value': 0}))