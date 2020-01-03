from M0_Gtalk.Gtalk import gtalk as gt
from M2_VTTV.VTTV import text_voice as v
from M1_Task.Task import task as tsk

if __name__ == "__main__":
   # gt.wishMe()
    while True:
        ans = v.takeCommand().lower()
        if  'jarvis' in ans :
          query = v.takeCommand().lower()
          tsk.execute(query)
        
        
