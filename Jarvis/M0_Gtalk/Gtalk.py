import datetime
import sys  
sys.path.append('D:\Project\Jarvis_Assitant')  
from M2_VTTV.VTTV import text_voice as v
    
class gtalk(object):
    
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            v.speak("Good Morning!")

        elif hour>=12 and hour<18:
            v.speak("Good Afternoon!")   

        else:
            v.speak("Good Evening!")  

        v.speak("I am Jarvis. Please tell me how may I help you") 
