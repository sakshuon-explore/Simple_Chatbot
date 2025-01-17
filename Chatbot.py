#question:answer
import time
now = time.ctime(2)

qna = {
    "hi":"hey",
    "how are you":"I am fine",
    "what is your name?":"My name is Eliza-The Bot",
    "what you do?":"I help the visitors to clarify there doubts",
    "what are the branches in BTech?":"AI,CSE,Civil,Electrical,ECE,Automation",
    "you need any help?":"No thankyou! Bye",
    "what is the time now?":now,
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])