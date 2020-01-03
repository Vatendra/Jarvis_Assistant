import sys
sys.path.append('D:\Project Git Hub\Jarvis_Assistant\Jarvis')  
from M2_VTTV.VTTV import text_voice as v

class format:
    def set_format():
        info={}
        v.speak("Hello Doctor, what is Patient's name")
        info.update({"Name":v.takeCommand().lower()})

        v.speak("What is the age")
        info.update({"Age":v.takeCommand().lower()})

        v.speak("What are the Symptons")
        info.update({"Problem":v.takeCommand().lower()})

        v.speak("What are the Diagnosis")
        info.update({"Diagnosis":v.takeCommand().lower()})

        v.speak("What are the Prescriptions")
        info.update({"Prescriptions":v.takeCommand().lower()})

        v.speak("Any advice doctor")
        info.update({"advice":v.takeCommand().lower()})

        
        

        print(str(info))

        v.speak("Thanks for the information") 




