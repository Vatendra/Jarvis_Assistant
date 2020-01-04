class file_op:
  def write_text(query):
    myfile = open('doc.txt', 'w')
    for x, y in query.items():
      myfile.write(x+':'+y+'\n')
    myfile.close()  


    