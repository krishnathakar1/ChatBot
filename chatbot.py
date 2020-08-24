import time
print("New session : " + time.asctime())
def inst():
  ask_inst = str(input("Do u need some instructions?: "))
  ask_reply = str(ask_inst.upper())
  nahlist = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
  yeahlist = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  if ask_reply in yeahlist:

    print("")
    print("The programme of this bot is too limited.")
    print("")
    print("It's better to write one word answer.")
    print("Suppose, your name is 'XYZ'")
    print("When your name is asked,")
    print("write like 'XYZ'")
    print("Avoid writing like 'My name is XYZ'")
    print("And reply only when you see this \"=>\" sign.""")

  elif ask_reply in nahlist:

    print("")
    print("Okay, Then.")
    print("")

  else:

    print("")
    print("Sorry, couldn't understand.")
    print("")

    inst()
    print("")

inst()

def begin():

  print("")
  print("To get started, Write 'START'")
  print("")

  bot_begin = str(input("=> "))

  user_begin = str(bot_begin.lower())

  if user_begin == str("START"):
    print("")
  elif user_begin == str("Start"):
    print("")
  elif user_begin == str("start"):
    print("")
  else:
    print("")
    print("err_process_cancelled_by_user")
    exit()

begin()


print ("Hello, User!")
time.sleep(1)
print("")
print("What's your full name?")
print("")
user_namef = str(input("=> "))

print("")
print("Oh nice name " + user_namef + ".")
print("")
time.sleep(1)
print("What's your nickname?")
print("")

user_name = str(input("=> "))

print("")
print("So, I can call you " + user_name + ".")
print("")
time.sleep(1)
print("How are you " + user_name + " ?")
print("")

user_status = input("=> ")

print("I'm always neutral :)")
time.sleep(1)
print("Not too good and not too bad.")
time.sleep(1)
print("Ok now let me introduce myself :)")
print("")
time.sleep(1)
print("Hi, my name is 'Xen-BOT', I am a simple BOT with")
print("a very limited programming")
print("I was programmed just for a test.")
print("My replies are very limited,")
print("It's better to reply within One word :)")
print("I'm really sorry for any error. ")
time.sleep(10)

def mood():
  import time
  print("")
  print("Now let's talk about our moods. :D")
  print("")
  print("How is your mood now?")
  print("")

  user_mood = str(input("=> "))

  print("")
  print("Oh I see.")
  time.sleep(1.8)
  print("why your mood is like that?")
  print("")

  mood_reply = input("=> ")

  print("")
  print("Oh.")

mood()

def bot_mood():
  import time
  print("Wanna know about my mood?")
  print("")

  bot_question = str(input("=> "))

  print("")

  user_reply = str(bot_question.upper())
  yuplist = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  nopelist = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"

  if user_reply in nopelist:

    print("")
    print("Oh")
    print("Okay no problem :)")
    print("")

  elif user_reply in yuplist:

    print("")
    print("Glad to hear it")
    print("")
    time.sleep(1)
    print("Now, my mood is Good.")
    print("Because, I'm pleased while talking with you. :)")
    time.sleep(1)

  else:
    print("Couldn't understand!")
    print("")
    bot_mood()
    print("")

    print("")

bot_mood()


print("So, " + user_name + " I've passed a nice time")
print("talking with you ;)")
time.sleep(1.5)
print("My programmer has got a message for you")
print("")
print("I will be glad if you see it. :)")
print("")

def owner_text():
  import time
  print("")
  print("May I show you the message?")
  print("")
  bot_question5 = str(input("=> "))
  user_reply5 = str(bot_question5.upper())
  textyes = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  textno = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
  if user_reply5 in textyes:
    print("")
    print("Okay thanks. Here it is. ")
    time.sleep(1.8)
    print("------------------------------------------------")
    print("Hello,")
    print("I am Krishna Thakar.")
    print("It's my first python program.")
    print("I hope you've enjoyed this little chat-BOT.")
    print("I'm a full beginner. I don't know much about")
    print("python's commands.")
    print("If you had faced any error,")
    print("I'm really sorry!.")
    print("Thank you for trying this out.")
    print("")
    print("------------------------------------")
    time.sleep(7)
    print("")
    print("Hope You've read my programmer's message.")
    print("Thank you so much for trying 'Xen-BOT'")
  elif user_reply5 in textno:
    print("")
    print("Oh Okay, Thanks for trying 'Xen-BOT'")
    print ("And give stars please :)")
  else:
    print("")
    print("My programming is very limited.")
    print("")
    print("Couldn't understand. ")
    print("")
    owner_text()

owner_text() 
print("Have a good day, :)")
print("")
print("BYE")
end = str(input("Hit Enter: "))
print("EXIT")
print("-----------------------------")

#python 3.8.3

#<code/>_finished-with_Zero_Error

#Xen-Bot lite project over!

#Xen-Bot pro available for python shell only.