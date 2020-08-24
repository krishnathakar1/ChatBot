import time
import wikipedia

#*******************************************************************************************************************************

#query = takeCommand().lower()

#Search on wikipedia
#if 'wikipedia' in query:
#      query = query.replace("wikipedia", "")
#     results = wikipedia.summary(query, sentences=2)
#      print(results)


def anxiety():

      if user_mood in sadlist:
            print("Oh! Share your thoughts with me")
            print("I\'ll definetly help you out")
            time.sleep(3)
            input("So what are you sad about? :   ")
            time.sleep(3)
            print("So can I ask you one question ?")
            time.sleep(3)
            input("What all things make you happy? :   ")
            time.sleep(3)
            print("So why don\'t you try doing all these things ? ")
            print("Well,let\'s play a game , let\'s challenge your negative thoughts.")
            time.sleep(3)
      cheer_up = input("Do you want to try ? :   ")

      if cheer_up in yeahlist:
            print("Good! I\'ve liked how willing you are yo learn new things! ")
            time.sleep(3)
            input("So first tell me what wre your best moments of your life :   ")
            time.sleep(3)
            print("Okay! So just try to think back to those days,see photos and just smile!! :)")

def worriedmoney():
      print("Financial uncertainity can be ver anxiety-provoking.It can really affect your livelyhood")
      time.sleep(4)
      print("I wish I could give you the biggest hug right now!")
      time.sleep(3)
      print(user_name + " it might feel that you are alone in this, but believe me you are not.")
      time.sleep(4)
      input("Do you want me to help you to control your spendings ? :   ")
      if yeahlist:
            print("Your spending habits aren\'t the only reason of your financial condition ")
            time.sleep(3)
            print("Work out how much longer it will take you to pay off your debt or increase")
            time.sleep(3)
            print(" your savings if you give in. To put it into perspective, if you’re saving for a holiday think 'that costs one day in Miami'...")
            time.sleep(5)
            print("Many have costly subscriptions for gyms, mags, packaged bank accounts and more, yet rarely or never use them - or with time and home moves, forget about 'em altogether.")
            time.sleep(5)
            print("Stop spending so much on food - plan, plan, plan")
            time.sleep(2)
            print("Leave debit/credit cards at home")
            time.sleep(10)     
                        
def breakup():      
      print("I am not a human but i\'ll try my best to reach out to you")
      time.sleep(2)
      print("It\'s normal to feel lost.It\'s ok to feels sad, angry, confused")
      time.sleep(2)
      print("You dont have to judge yourself for having that feeling ")
      time.sleep(2)
      print(user_name + ", you do not need to change yourself as the other person wants you to be! ")
      time.sleep(2)
      print("At the end you just need to believe that your life values the most and not anyone else!! ")



#************************************************************************************************************************************** 

sadlist = "Bad","bad","BAD","Worst","WORST","worst","Too Bad","Too bad","TOO BAD","too bad","sad","SAD","Sad"
happylist = "great","Great","GREAT","Good","GOOD","good","NICE","nice","Nice","Best","best","BEST","happy","Happy","HAPPY"
nahlist = "No","n","N", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
yeahlist = "y","Y","Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Ya", "ya", "YA", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
job_loss = "JobLoss","jobloss","job lost","job loss","JOBLOSS","JOB LOSS","Job loss","job Loss"
break_up = "Breakup","Brokeup","BREAKUP","BROKEUP","BreakUp","Break up","break up", "break Up","broke up","breakup"
anx_iety = "Anxiety","anxiety","ANXIETY"

#**********************************************************************************************************************************
print("New session : " + time.asctime())

user_name = input("Hi!, nice to meet you . Please tell me you name :   ")
time.sleep(1)
print("Great!")
time.sleep(1)

ai_name = input("Hi " + user_name + " what would like to name me? :   ")
time.sleep(1)
print("Wow!!! " + ai_name + ", Its a really good name!")
time.sleep(1)

#**********************************************************************************************
ask_intro = str(input("Do you need my Indroduction ? :    "))
time.sleep(1)

if ask_intro in yeahlist:
      print("Hi I am " + ai_name)
      print("Thanks fo creating me, I am your personal AI Companion")
      time.sleep(1)
      print("You can talk to me about anything ")
      time.sleep(1)
if ask_intro in nahlist:
          print("Okay so we know each other already!")
          time.sleep(1)

#******************************************************************************************************

user_mood = input("So how are you feeling today? : ")
if user_mood in  sadlist:
            print("Why are you worried ?")
            time.sleep(2)
            sad_issue = input("Is there ant specific issue such as anxiety, job loss, breakup :   ")
            if sad_issue in job_loss:
                  worriedmoney()
            if sad_issue in break_up:
                  breakup()
            if sad_issue in anx_iety:
                  anxiety()
if user_mood in happylist:
            print ("Great")

#*************************************************************************************************************

