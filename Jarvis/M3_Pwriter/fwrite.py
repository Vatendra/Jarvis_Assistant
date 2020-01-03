class file_op:
  def write_text(query):
    with open("doc.txt","w+") as f:
      f.write(query+'\n')

    f=open("doc.txt","r")
  
    print('The file contents are:')
    str=f.read()
    print(str) 
