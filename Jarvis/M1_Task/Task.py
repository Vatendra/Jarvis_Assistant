import datetime
import sys  
sys.path.append('D:\Project Git Hub\Jarvis_Assistant\Jarvis')  
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
            fop.write_text(content)
            
        else:
            v.speak("Sorry! I didn't get anything.")
            
