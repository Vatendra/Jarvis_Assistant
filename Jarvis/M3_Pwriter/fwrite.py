from M2_VTTV.VTTV import text_voice as v
import datetime as dt
class file_op:
  def write_text(query):
    #myfile = open('doc.txt', 'w')
    v.speak("Doctor! , can I add your details to the Patient form!")
    a=v.takeCommand().lower()
    flag=0
    if 'yes' in a:
      flag+=1
      with open("pers.txt") as f:
        with open("doc.txt", "w") as f1:
          for line in f:
            f1.write(line)
            
    if flag == 1:
      f1=open("doc.txt", "a")
      f1.write("Patient Details:"+"\n\n")
      for x, y in query.items():
          f1.write(x+':'+y+'\n')
      f1.write('Date :%s'%(dt.date.today()))
      
    else:
      f1=open("doc.txt", "w")
      f1.write("Patient Details:"+"\n\n")
      for x, y in query.items():
        f1.write(x+':'+y+'\n')
      f1.write('Date :%s'%(dt.date.today()))

  def write_detail(query):
    myfile = open('pers.txt', 'w+')
    myfile.write("___________________________"+"\n"+"----------------------"+"\n")
    for x in query:
      if x != 'None':
        myfile.write(x+"\n")
    myfile.write("___________________________"+"\n"+"----------------------"+"\n\n")
    
