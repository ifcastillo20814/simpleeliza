#Simple Eliza program
while True:
    chat = input ("Good day. What is your problem? Enter your response here or Q to quit:")
                   
    print(chat) 

    chatCont = input ("Enter your respose here or Q to quit: ")
    print (chatCont)
                  
    if chatCont.upper().startswith("Q"):
       print("you exit to chat!")
       exit()
                                                 



                


