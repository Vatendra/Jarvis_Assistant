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

        v.speak("What can I retrieve for you!")
        query = v.takeCommand().lower()

        if 'all' in query:
            for x in mycol.find():
                print(x)
                print()
    
        elif 'name wise' in query:
            key = "Name"
            v.speak("Please,enter name of patient ")
            val = input("Enter Name for details:").title()
            det = {key:val}
            for x in mycol.find(det):
                print(x)
                print()
            
        elif 'gender wise' in query:
            key = "Gender"
            v.speak("Please, Enter gender of patient")
            val = input("Enter Gender for details:").title()
            det = {key:val}
            for x in mycol.find(det):
                print(x)
                print()

        elif 'age wise' in query:
            key = "Age"
            v.speak("Please , Enter age of patient")
            val = int(input("Enter Age for details:"))
            det = {key:val}
            for x in mycol.find(det):
                print(x)
                print()


        elif 'disease wise' in query:
            key = "Diagnosis"
            v.speak("Please , Enter diagnosis of patient")
            val = input("Enter Diagnosis for details:").title()
            det = {key:val}
            for x in mycol.find(det):
                print(x)
                print()

        
            
