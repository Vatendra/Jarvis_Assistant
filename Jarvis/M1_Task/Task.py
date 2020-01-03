import datetime
import sys  
sys.path.append('D:\Project\Jarvis_Assitant')  
from M2_VTTV.VTTV import text_voice as v
from M3_Pwriter.fwrite import file_op as fop

class task:
    def execute(query):
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            v.speak(f"Sir, the time is {strTime}")
            
        elif 'cription' in query:
            v.speak("Please speak your contents")
            query = v.takeCommand()
            fop.write_text(query)
            
        else:
            v.speak("Sorry! I didn't get anything.")
            
