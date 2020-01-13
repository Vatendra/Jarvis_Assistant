from pymongo import MongoClient
from M2_VTTV.VTTV import text_voice as v

class Database_Insert:

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
    
   

class Database_Retrieve:

   
    def retrive():
        client = MongoClient('localhost',27017)
        mydb = client["Jarvis"]
        mycol = mydb["details"]
        
        v.speak('here are the keywords')
        print('1.Name\n2.Gender\n3.Age\n4.Diagnosis\n5.Date')
        query=input('Enter the keyword:').title()
       
        if 'Date' in query:
         value=input('Enter the corrosponding value:')
         
        else:
         value=input('Enter the corrosponding value:').title()
        
        myquery={query:{"$regex":value}}
         
        for x in mycol.find(myquery):
                print(x)
       
       
      