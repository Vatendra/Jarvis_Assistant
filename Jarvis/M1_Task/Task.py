import datetime
import sys  
sys.path.append('D:\Project Git Hub\Jarvis_Assistant\Jarvis')
from M5_PDFG.pdfg import pdf_converter as pdf  
from M2_VTTV.VTTV import text_voice as v
from M3_Pwriter.fwrite import file_op as fop
from M3_Pwriter.formatter import format as fw

class task:
    def execute(query):
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            v.speak(f"Sir, the time is {strTime}")
            
        elif 'cription' in query:
            content=fw.set_format()
            v.speak(content)
            v.speak('Do you want to edit')
            query=v.takeCommand().lower()
            if 'yes' in query:
                 v.speak('you want to add or delete an entry')
                 query=v.takeCommand().lower()
                 if 'delete' in query: 
                   v.speak('whick entry you want to delete')
                   k=v.takeCommand().title()
                   del content[k]
                 if 'add' in query:
                     v.speak('say the key')
                     key=v.takeCommand().title()
                     v.speak('say the value')
                     value=v.takeCommand().lower()
                     content.update({key:value})
            fop.write_text(content)
            pdf.generate_pdf()
            
            
        else:
            v.speak("Sorry! I didn't get anything.")
            
