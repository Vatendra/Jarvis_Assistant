import sys
sys.path.append('D:\Project Git Hub\Jarvis_Assistant\Jarvis')
from pymongo import MongoClient
import csv

class tocsvfile():
 
 def export(): 
     client = MongoClient('localhost',27017)
     mydb = client["Jarvis"]
     mycol = mydb["details"]

     
     csv_reader=mycol.find({},{'_id':0})
     csv_reader=list(csv_reader)
     

     with open('Patients_record.csv','w',newline='') as new_file:
             fieldnames=['Name','Gender','Age','Problem','Diagnosis','Prescriptions','Advice','Date']
             csv_writer=csv.DictWriter(new_file,fieldnames)
             
             csv_writer.writeheader()

             csv_writer.writerows(csv_reader)
     