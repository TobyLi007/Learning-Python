from pymongo import MongoClient
from pymongo import ASCENDING

client = MongoClient('mongodb://127.0.0.1:27017') 
db = client.school

for student in db.students.find():
    print('学号:', student['stuid'])
    print('姓名:', student['name'])
    print('电话:', student['tel'])

db.students.find().count()
db.students.remove()
db.students.find().count()

coll = db.students

coll.create_index([('name', ASCENDING)], unique=True)
coll.insert_one({'stuid': int(1001), 'name': '骆昊', 'gender': True})
coll.insert_many([{'stuid': int(1002), 'name': '王大锤', 'gender': False}, {'stuid': int(1003), 'name': '白元芳', 'gender': True}])
for student in coll.find({'gender': True}):
    print('学号:', student['stuid'])
    print('姓名:', student['name'])
    print('性别:', '男' if student['gender'] else '女')