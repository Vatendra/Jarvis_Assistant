import datetime as dt
class file_op:
  def write_text(query):
    #myfile = open('doc.txt', 'w')
    with open("pers.txt") as f:
      with open("doc.txt", "w") as f1:
        for line in f:
            f1.write(line)
        f1.write("Patient Details:"+"\n\n")
        for x, y in query.items():
          f1.write(x+':'+y+'\n')
        f1.write('Date :%s'%(dt.date.today()))  

  def write_detail(query):
    myfile = open('pers.txt', 'w+')
    myfile.write("___________________________"+"\n"+"----------------------"+"\n")
    for x in query:
      if x != 'None' or 'No' not in x:
        myfile.write(x+"\n")
    myfile.write("___________________________"+"\n"+"----------------------"+"\n\n")
    
