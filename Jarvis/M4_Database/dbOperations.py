from pymongo import MongoClient

class Database:

    def Insert():
        client = MongoClient('localhost',27017)
        mydb = client["Jarvis"]
        mycol = mydb["details"]

        d = {}
        with open("doc.txt") as f:
            while True: 
                a = f.readline()
                if not a:
                    break
                else:
                    a = a.split(':')
                    try:
                        key = a[0]
                        val = a[1].strip('\n')
                        d.update({key:val})
                    except:
                        pass
            #print(d)
        x = mycol.insert_one(d)
        #for x in mycol.find({},{"_id":0,"Name":1,"Age":1}):
            #print(x)
            #print()

