
import time
import sys
import os
from os import system


def next():
    item = ["",
            "",
            "",
            "Type next to continue",
            ""]

    for texts in item:
        for char in texts:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

    next = input()
    while next != "next":

        prompt =  "That is not a valid input. When you are ready to go back to the title screen, type 'next'."
        for char in prompt:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.07)
        next = input()

    if next=="next":
        pass



def title_screen():


    os.system('clear')
    swordlist = [
    "████████╗██╗░░██╗███████╗",
    "╚══██╔══╝██║░░██║██╔════╝",
    "░░░██║░░░███████║█████╗░░",
    "░░░██║░░░██╔══██║██╔══╝░░",
    "░░░██║░░░██║░░██║███████╗",
    "░░░╚═╝░░░╚═╝░░╚═╝╚══════╝",
    "██████╗░██╗░░██╗██╗██╗░░░░░░█████╗░░██████╗░█████╗░██████╗░██╗░░██╗███████╗██████╗░██╗░██████╗",
    "██╔══██╗██║░░██║██║██║░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗╚█║██╔════╝",
    "██████╔╝███████║██║██║░░░░░██║░░██║╚█████╗░██║░░██║██████╔╝███████║█████╗░░██████╔╝░╚╝╚█████╗░",
    "██╔═══╝░██╔══██║██║██║░░░░░██║░░██║░╚═══██╗██║░░██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗░░░░╚═══██╗",
    "██║░░░░░██║░░██║██║███████╗╚█████╔╝██████╔╝╚█████╔╝██║░░░░░██║░░██║███████╗██║░░██║░░░██████╔╝",
    "╚═╝░░░░░╚═╝░░╚═╝╚═╝╚══════╝░╚════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═════╝░",
    "██╗░░░░░░█████╗░███╗░░██╗██████╗░",
    "██║░░░░░██╔══██╗████╗░██║██╔══██╗",
    "██║░░░░░███████║██╔██╗██║██║░░██║",
    "██║░░░░░██╔══██║██║╚████║██║░░██║",
    "███████╗██║░░██║██║░╚███║██████╔╝",
    "╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░(█)░░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░░(█)░░░░░░",
    "░░░░(██)░░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░░(██)░░░░░",
    "░░░(██)░░░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░░░(██)░░░░",
    "░░(██)░░░░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░░░░(██)░░░",
    "░░(███)░░░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░░░(███)░░░",
    "░░░(████)░░░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░░░(████)░░░░",
    "░░░░(█████)░░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░░(█████)░░░░░",
    "░░░░░(█████)░░░░░░░░░░░░░░░(█████)░░░░░░░░░░░░░░░(█████)░░░░░░",
    "░░░░░░(█████)░░░░░░░░░░░░(█████████)░░░░░░░░░░░░(█████)░░░░░░░",
    "░░░░░░░░(███████)░░░░░░(█████████████)░░░░░░(███████)░░░░░░░░░",
    "░░░░░░(███████████████████████░███████████████████████)░░░░░░",
    "░░░░░░░░░░░░(████████████████░░░████████████████)░░░░░░░░░░░░",
    "░░░░░░░(██████████████████████████████████████████████)░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░(█████████████████)░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(███████)░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(███████████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(███░░░░░░░███)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(███░░░░░███)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░(█░░░░███░███░░░░█)░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░(███████^███████)░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(███^███)░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(█░░███^███░░█)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░(█░░░░(███^███)░░░░█)░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░(██░░░░███^███░░░░██)░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░(████████^████████)░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(███^███)░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░(██████^██████)░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░(█████^█████)░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░(████^████)░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(███^███)░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(███^███)░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░(███^███)░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░(██^██)░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░(██^██)░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░(██^██)░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░(█^█)░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░(█^█)░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░(███)░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░(█)░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "▒█▀▀█ █░░ █▀▀█ █░░█ ░░ ▒█░▒█ █▀▀ █░░ █▀▀█ ░░  ▒█▀▀█ █░░█ ░█░ ▀▀█▀▀",
    "▒█▄▄█ █░░ █▄▄█ █▄▄█ ▄▄  ▒█▀▀█ █▀▀ █░░ █░░█ ▄▄  ▒█░▒█ █░░█ ░█░ ░░█░░",
    "▒█░░░ ▀▀▀ ▀░░▀ ▄▄▄█ ░█  ▒█░▒█ ▀▀▀ ▀▀▀ █▀▀▀ ░█  ░▀▀█▄ ░▀▀▀ ░█░ ░░▀░░"]

    for item in swordlist:
        for char in item:
            sys.stdout.write(char)
            time.sleep(0.001)
        print("")






    choice = input()

    while choice not in ["HELP","Help","help","QUIT","quit","Quit","PLAY","play","Play"]:
        prompt =  "That is not a valid input. Please type Play, Quit or Help."
        for char in prompt:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        choice = input()



    if choice in ["HELP","Help","help"]:
        help()
    if choice in ["QUIT","quit","Quit"]:
        quit()
    if choice in ["PLAY","play","Play"]:
        play()


    #input the start function, help function and quit function for the valid choices.
    #In final function, let title screen go first



def help():

    os.system('clear')
    instructions = [
    "The philsophers land is a text based adventure game.",
    "All your choices will have to be typed according to the prompt given.",
    "You will see a series of ######### before being asked to make a choice",
    "If you don't type accoriding to the prompt, don't panic. you will be asked to type again.",
    "Some things to remember : ",
    "",
    "Every action is irreversible, you will not be able to undo a choice.",
    "Once you enter the land, there is no leaving unless you fulfill your destiny.",
    "Choices you make have significant effects. They can change the way characters in this world interact with you.",
    "",
    "All your actions have consequences",
    "Choose Wisely."
    "",
    "When you are ready to go back to the title screen, type 'back'."]

    for item in instructions:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

    back = input()
    while back != "back":

        prompt =  "That is not a valid input. When you are ready to go back to the title screen, type 'back'."
        for char in prompt:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.07)
        back = input()

    title_screen()




def quit():
    os.sytem('exit')



def intro():
    os.system('clear')
    description = ["You wake up from what has felt like one of those naps that transform you into another dimension.",
                  "From your blurry vision, you see an old man crouching over you.",
                  "He seems to be examining you.",
                  "With glistening eyes and a wrinkly forehead, he finally screams",
                   "",
                  "Old man : It's You! It really is YOU!",
                  "Wait what, Who am I? I don't know what you are talking about.",
                  "Old man : What do you mean you don't know? You are here to fulfill the prophecy!",
                   "",
                   "#######################",
                   "Option 1 : WHERE EVEN AM I ?",
                   "Option 2 : What Prophecy?!",
                   "Option 3 : Can I just go home ",
                   "Type 1,2 or 3 to choose your option.",
                   "#########################"

                  ]
    for item in description:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")


    answer1= input()

    while answer1 not in ['1', '2', '3']:
        prompt=["Please enter a valid input.",
                   "#########################",
                   "Option 1 : WHERE EVEN AM I ?",
                   "Option 2 : What Prophecy?!",
                   "Option 3 : Can I just go home ",
                   "Type 1,2 or 3 to choose your option.",
                   "#########################"]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")
        answer1= input()


    if answer1 == '1':
        list1=["Hold on. WHERE EVEN AM I?!",
        "Old man : Oh.....How foolish of me. I completely forgot to welcome you.",
        "You are in The Philosopher's land.",
        "The land of thought, ideas, a little bit of nihilism here and there but we get through.",
        "Our land used to be peaceful and quiet, but for a few years we have been terrorsied by an evil demon.",
        "Our philosophers have been in a state of constant fear since he arrived and according to the prophecy,",
        "YOU are the only one that can save us!",
        "Tell me boy, what is your name"]

        for item in list1:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        name = input()


    if answer1 == '2':
        list2 = ["What are you on about? I don't know of any prophecy!",
        "Old man : Oh.....of course you don't. Let me explain.",
        "Old man : You are in The Philosopher's land.",
        "Old man : The land of thought, ideas, a little bit of nihilism here and there but we get through.",
        "Old man : Our land used to be peaceful and quiet, but for a few years we have been terrorsied by an evil demon.",
        "Old man : Our philosophers have been in a state of constant fear since he arrived and according to the prophecy,",
        "Old man : YOU are the only one that can save us!",
        "Old man : Tell me boy, what is your name"]

        for item in list2:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")


        name = input()

    if answer1 == '3':

        list3 = ["I just want to go home.",
        "Old man : GO HOME?! WHAT RUBBISH. YOU HAVE TO SAVE US.",
        "Old man : Sorry, I shouldn't be shouting at our saviour. Let me explain.",
        "Old man : You are in The Philosopher's land.",
        "Old man : The land of thought, ideas, a little bit of nihilism here and there but we get through.",
        "Old man : Our land used to be peaceful and quiet, but for a few years we have been terrorsied by an evil demon.",
        "Old man : Our philosophers have been in a state of constant fear since he arrived and according to the prophecy,",
        "Old man : YOU are the only one that can save us!",
        "Old man : Tell me boy, what is your name"]

        for item in list3:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        name = input()


    get_rigged=["Old man : Ah,"+name+". Sounds like the name of our saviour.",
               "Old man : So "+name+" let me give you what I can to help you venture through the land.",
               "Old man : Here, take my sword. It is sharp, but not fatal.",
               "Old man : Remember, in the philosophers land, we fight with our thougts.",
               "Old man : This is a map of all the places you must visit to complete the quest. Follow it.",
               "Old man : I don't have any human food on me, but you can have my cat's tuna.",
               "Old man : Uhh, what else can I provide?",
               "Old man : Oh yes! Philosophical advice, of course.",
               "Old man : Remember "+name,
               "Old man : Your actions have consequences. Choose Wisely.",
               "Old man : Are you ready?",
                "#########################",
                   "Option 1 : I'm ready! Let's go.",
                   "Option 2 : What Evil Demon? Is this thing even human?!",
                   "Option 3 : Can I just go home",
                   "Type 1,2 or 3 to choose your option.",
                   "#########################"]


    for item in get_rigged:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")



    answer2 = input()

    while answer2 not in ['1','2','3']:
        prompt=["Please enter a valid input.",
                    "#########################",
                   "Option 1 : I'm ready! Let's go.",
                   "Option 2 : What Evil Demon? Is this thing even human?!",
                   "Option 3 : Can I just go home",
                   "Type 1,2 or 3 to choose your option.",
                   "#########################"]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

    if answer2 == '1':
        list1= ["I'm ready! Let's go.",
        "Old man : I'm glad to hear that. Follow the map and fulfil your destiny."]


        for item in list1:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")




    if answer2 == '2':
        list2 = ["What Evil Demon? Is this thing even human?!",
        "Old man : I can't reveal anything, you must find out for yourself.",
        "Old man : Off you go now, follow the map and fulfil your destiny.",
        ]

        for item in list2:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")




    if answer2 == '3':

        list3 = ["I just want to go home.",
        "Old man : I can't believe our saviour is such a coward.",
        "Old man : There is no home until you save the land.",
        "Old man : Off you go now, follow the map and fulfil your destiny.",
         ]

        for item in list3:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

    return name



# In[236]:


def cat():
    os.system('clear')

    cat_intro=["You open the map and find that you have to walk towards the mountains.",
              "Looking around, you can see them towering over the rest of the landscape.",
              "As you begin walking towards the mountains, you hear a sound in the bushes.",
               "",
              "Who is there?! You ask.",
               "",
              "The rustling of the bush intensifies.",
               "",
              "Come Out and FACE ME!",
               "",
              "You recieve no response.",
              "",
              "#######################",
              "Option 1 : inspect ",
              "Option 2 : keep walking",
              "Type 1 or 2 to select.",
              "#########################"
              ""]
    for item in cat_intro:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")


    answer1 = input()


    while answer1 not in ['1','2','3']:
        prompt=["Please enter a valid input.",
                    "#########################",
              "Option 1 : inspect ",
              "Option 2 : keep walking",
              "Type 1 or 2 to select.",
              "#########################"
               ""]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer1 = input()


    if answer1 == '1':
        list2 = ["You go closer to the bushes",
                 "The sound intensifies further",
                 "You push your way through some of the leaves and peek in",
                 "To find a small kitten quivering in fear",
                 "",
                 "Awww! It's just a kitten you exclaim",
                 "Kitten : purr!",
                 "",
                 "She seems to be trembling with fear, but still is in a position of attack",
                 "",
                 "#########################",
              "Option 1 : scare with sword ",
              "Option 2 : give the old man's tuna",
              "Type 1 or 2 to select.",
              "#########################"
                 ""
        ]

        for item in list2:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer2 = input()

        while answer2 not in ['1','2']:
            prompt=["Please enter a valid input.",
                    "#########################",
              "Option 1 : scare with sword ",
              "Option 2 : give the old man's tuna",
              "Type 1 or 2 to select.",
              "#########################"
                   ""]
            for item in prompt:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

            answer2 = input()

        if answer2 == '1':
            cat_attitude = "bad"
            list1=["The kitten shrieks and runs away.",
                   "",
                  "Well, if the Evil Demon is anything like that, I have this under control.",
                  "To the mountains!"]

            for item in list1:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")


        if answer2 == '2':
            cat_attitude = "good"
            list1=["You slowly inch closer.",
                  "The kitten is suspicious of your actions, she hisses at you.",
                   "",
                  "It's Okay, Look! I have food for you!",
                   "",
                  "You slowly pull out the tuna",
                  "The kitten relaxes, she inches closer",
                   "",
                  "Here you go, you say while keeping the tuna on the grass.",
                   "",
                  "She instantly jumps over it and gobbles it up",
                   "",
                  "Oh wow, someone was hungry! you say as she licks any leftovers.",
                   "",
                  "The kitten looks up at you with thankful eyes",
                   "",
                   "Kitten : Meow (affectionate)"
                   "",
                  "As you reach to pet her",
                  "She instantly runs away",
                   "",
                  "Classic.",
                   "Off to the mountains!"]

            for item in list1:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")





    if answer1 == '2':
        cat_attitude="bad"

        list3 = ["I dont have time for this.","Off to the mountains!"
         ]

        for item in list3:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

    return cat_attitude




def decartes(name):
    os.system('clear')

    decartes_intro =["You venture your way into the mountains for what feels like a lifetime.",
                    "",
                    "I could use some warmth, you think to yourself as the wind sends chills down your spine",
                    "",
                    "As you reach the foothills, you see a small house",
                    "The house is tiny, but comforting",
                    "It has a red brick exterior with a chimney letting out series of smoke."
                    "",
                    "A fireplace! you think to yourself",
                    "",
                    "Desperate for some warmth, you decide to enter the house.",
                    "#####################",
                    "Option 1 : Knock",
                    "Option 2 : Invite yourself in",
                    "Type 1 or 2 to select.",
              "########################",""]

    for item in decartes_intro:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

    answer1 = input()

    while answer1 not in ['1','2']:
        prompt=["Please enter a valid input.",

              "#####################",
                    "Option 1 : Knock",
                    "Option 2 : Invite yourself in"
                    "Type 1 or 2 to select.",
              "########################",
                   ""]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer1 = input()

    if answer1 == '1':
        decartes_attitude1="good"
        list1=[ "You knock on the door",
                   "",
                   "Anyone there?",
                   "",
                   "You recieve no response.",
                   "You knock again and the door creaks open a little",
                  "",
                   "You see a strange man, seated by the fire",
                   "Attired in a dressing gown",
                   "Having a paper in his hand",
                   "In deep thought, almost as if he is meditating, he keeps repeating the phrase:",
                   "",
                   "Strange Man : I think, therefore I am.",
                   "",
                   "He hears you creek open the door and looks you up and down.",
                   "",
                   "Strange Man : Oh, wow, you're finally here.",
                   "I'm sorry, who are you?",
                   "Strange Man : Who am I? Oh my boy, I am simply my thoughts.",
                   "Strange Man : I mean, aren't we all.",
                   "You seem to be visibily confused by him.",
                   "Strange Man : So the saviour isn't from the land of philosopy I suppose.",
                   "Strange Man : Let me re-introduce myself.",
                   "Strange Man : I am Rene Decartes, your first step to save our land.",
                   "Oh. Okay. I am-",
                   "Decartes : I know exactly who you are "+name,"Tell me now, are you a Dualist or a Duelist?",
              "#####################",
                    "Option 1 : Dualist",
                    "Option 2 : Duelist",
                    "Type 1 or 2 to select.",
              "########################",
                   ""]



        for item in list1:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer2 = input()

        while answer2 not in ['1','2']:
            prompt=["Please enter a valid input.",

                   "#####################",
                    "Option 1 : Dualist",
                    "Option 2 : Duelist",
                    "Type 1 or 2 to select.",
                    "########################",
                   ""]
            for item in prompt:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

        if answer2 == '1':
            decartes_attitude2="good"

            dualist = ["Decartes : I KNEW IT!",
                          "Decartes : I KNEW THE CHOSEN ONE WOULD BE A DUALIST!",
                          "Decartes : Here you go boy",
                          "*He hands you a stone*",
                          "Decartes : You will have to collect more of these, that unlock a secret code",
                          "Decartes : Once the secret code is deciphered",
                           "Decartes : When said out loud, will give you a chance to summon the evil demon.",
                           "Decartes : And destroy him, once and for all.",
                          "But, if you know where the stones are, why wouldn't you just decipher it yourself?",
                          "Decartes : The evil demon is smarter than that.",
                          "Decartes : He has distributed the stones only to the philosophers that disagree with each other",
                          "Decartes: We would rather live in a land of terrror than co-operate",
                          "Decartes : Which leads you to your next subject",
                          "Decartes: My worst enemy himself",
                          "Decartes : esse est percipi, such a load of bullshit.",
                          "esse es-WHAT?",
                           "Decartes : irrelevant, off you go now. Follow the map.",
                          "Decartes : Good luck "+name]

            for item in dualist:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")


        if answer2 == '2':
            decartes_attitude2="bad"

            dualist = ["Decartes : WHY DO YOU CHOSEN ONES ALWAYS HAVE TO TAKE THE HARD WAY OUT",
                          "Decartes : I CAN'T BELIEVE YOU AREN'T A DUALIST!",
                        "Decartes : Well, now for the stone, you must defeat me in a duel.",
                        "*Pulls Out Sword*",
                              "Decartes : Show me what you got.",
                              "",
                              "You both engage in a rather gentleman's duel",
                              "After what feels like hours of respectful apologies and sword clinking",
                              "You manage to create a tear on Decarte's dressing gown",
                              "",
                              "Decartes : Ah, it seems as if I have lost.",
                            "Decartes : Here you go boy",
                          "*He hands you a stone*",
                          "Decartes : You will have to collect more of these, that unlock a secret code",
                          "Decartes : Once the secret code is deciphered",
                           "Decartes : When said out loud, will give you a chance to summon the evil demon.",
                           "Decartes : And destroy him, once and for all.",
                          "But, if you know where the stones are, why wouldn't you just decipher it yourself?",
                          "Decartes : The evil demon is smarter than that.",
                          "Decartes : He has distributed the stones only to the philosophers that disagree with each other",
                          "Decartes: We would rather live in a land of terrror than co-operate",
                          "Decartes : Which leads you to your next subject",
                          "Decartes: My worst enemy himself",
                          "Decartes : esse est percipi, such a load of bullshit.",
                          "esse es-WHAT?",
                           "Decartes : irrelevant, off you go now. Follow the map.",
                          "Decartes : Good luck "+name]

            for item in dualist:
                    for char in item:
                        sys.stdout.flush()
                        sys.stdout.write(char)
                        time.sleep(0.04)
                    print("")




    if answer1 == '2':
        decartes_attitude1="bad"
        list1=["You creek the door open",
                   "You see a strange man, seated by the fire",
                   "Attired in a dressing gown",
                   "Having a paper in his hand",
                   "In deep thought, almost as if he is meditating, he keeps repeating the phrase:",
                   "",
                   "Strange Man : I think, therefore I am.",
                   "",
                   "He hears you creek open the door and looks you up and down.",
                   "",
                   "Strange Man : Oh, is knocking on the door uncommon in your world?",
                   "I'm sorry, who are you?",
                   "Strange Man : Who am I? You unlearned human. I am simply my thoughts.",
                   "You seem to be visibily confused by him.",
                   "Strange Man : So the saviour isn't too smart I suppose.",
                   "Strange Man : Let me re-introduce myself.",
                   "Strange Man : I am Rene Decartes, your first step to save our land.",
                   "Oh. Okay. I am-",
                   "Decartes : I know exactly who you are " +name, "Tell me now, are you a Dualist or a Duelist?",

              "#####################",
                    "Option 1 : Dualist",
                    "Option 2 : Duelist",
                    "Type 1 or 2 to select.",
              "########################",
                   ""]



        for item in list1:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer2 = input()

        while answer2 not in ['1','2']:
            prompt=["Please enter a valid input.",
                   "#####################",
                    "Option 1 : Dualist",
                    "Option 2 : Duelist",
                    "Type 1 or 2 to select.",
                    "########################",
                   ""]


            for item in prompt:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

        if answer2 == '1':


            dualist = ["Decartes : I KNEW IT!",
                          "Decartes : INSPITE OF YOUR ILL MANNERS, I KNEW YOU WOULD BE A DUELIST",
                          "Decartes : Here you go boy",
                          "*He hands you a stone*",
                          "Decartes : You will have to collect more of these, that unlock a secret code",
                          "Decartes : Once the secret code is deciphered",
                           "Decartes : When said out loud, will give you a chance to summon the evil demon.",
                           "Decartes : And destroy him, once and for all.",
                          "But, if you know where the stones are, why wouldn't you just decipher it yourself?",
                          "Decartes : The evil demon is smarter than that.",
                          "Decartes : He has distributed the stones only to the philosophers that disagree with each other",
                          "Decartes: We would rather live in a land of terrror than co-operate",
                          "Decartes : Which leads you to your next subject",
                          "Decartes: My worst enemy himself",
                          "Decartes : esse est percipi, such a load of bullshit.",
                          "esse es-WHAT?",
                           "Decartes : irrelevant, off you go now. Follow the map.",
                          "Decartes : Good luck "+name]
            decartes_attitude2="good"

            for item in dualist:
                    for char in item:
                        sys.stdout.flush()
                        sys.stdout.write(char)
                        time.sleep(0.04)
                    print("")



        if answer2 == '2':


            dualist = ["Decartes : OF COURSE YOU AREN'T A DUALIST",
                          "Decartes : I knew the chosen one would be like one of those monoist imbeciles",
                        "Decartes : Well, now for the stone, you must defeat me in a duel.",
                        "*Pulls Out Sword*",
                              "Decartes : Show me what you got.",
                              "",
                              "You both engage in a rather aggressive duel",
                              "After what feels like hours of philosophical insults and sword clinking",
                              "He manages to create a tear on your dressing gown",
                              "",
                              "Decartes : Ah, it seems as if you have lost.",
                            "Decartes : Here you go, weakling",
                          "*He hands you a stone*",
                          "Decartes : You will have to collect more of these, that unlock a secret code",
                          "Decartes : Once the secret code is deciphered",
                           "Decartes : When said out loud, will give you a chance to summon the evil demon.",
                           "Decartes : And destroy him, once and for all.",
                          "But, if you know where the stones are, why wouldn't you just decipher it yourself?",
                          "Decartes : The evil demon is smarter than that.",
                          "Decartes : He has distributed the stones only to the philosophers that disagree with each other",
                          "Decartes: We would rather live in a land of terrror than co-operate",
                          "Decartes : Which leads you to your next subject",
                          "Decartes: My worst enemy himself",
                          "Decartes : esse est percipi, such a load of bullshit.",
                          "esse es-WHAT?",
                           "Decartes : irrelevant, off you go now. Follow the map.",
                          "Decartes : Good luck "+name]

            decartes_attitude2="bad"

            for item in dualist:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")


    return decartes_attitude2






def berkely(decartes_attitude2,name):
    os.system('clear')

    berkely_intro=["You open the map, to see that the next location is supposed to be right next door to this house.",
                  "You look around to see nothing but empty patches of land for acres and acres ahead.",
                   "",
                  "Well, that's weird.",
                  "",
                  "As you examine closer, you see a man, laying on the grass",
                  "He seems to be - in his own world",
                  "Hello? you call out",
                  "He looks up at you",
                  "",
                "Sir! I need some help finding my next location. Can you please help me navigate this map.",
                  "Strange Man : You don't have to find the next location boy",
                   "Well then? What? I can't just stop here",
                   "Strange Man : You misunderstand, you don't have to find it. You simply have to percieve it.",
                   "Strange Man : Come, take a seat."
                  ]
    for item in berkely_intro:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

    if decartes_attitude2=="good":

        berkely_intro2=["Strange Man : I see, you didn't duel Decartes",
                  "Strange Man : Well then, I guess my perception of you is worthless.",
                   "Your perception of me?",
                  "Strange Man : Oh wow, pretending as if monoism doesn't exist at all are we?",
                  "Monoism? I was told you are Decartes greatest enemy! What is all this talk about percieving?",
                  "",
                  "Strange Man : Oh he said that did he? I am Berkely, Decartes greatest opponent.",
                  "Berkely : I won't waste my time in changing your beliefs for at the end of the day",
                  "Berkely : It's all in my head anyway.",
                        "",
                   "He hands you the stone and walks away",
                  "People here are weird man, you think to yourself."
                  ]
        for item in berkely_intro2:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")


    else:
        berkely_intro2=["Strange Man : I see, you dueled Decartes",
                  "Strange Man : Well then, I guess my perception of you is a monoist.",
                   "Your perception of me?",
                  "Strange Man : To be is to be percieved, son. Isn't monosim what you believe in?",
                  "Monoism? I was told you are Decartes greatest enemy! What is all this talk about percieving?",
                  "",
                  "Strange Man : Oh he said that did he? I am Berkely, Decartes greatest opponent.",
                  "Berkely : I won't waste my time in explaining my belief for at the end of the day",
                  "Berkely : It's all in my head anyway.",
                        "",
                   "He hands you the stone and walks away",
                  "People here are weird man, you think to yourself."
                  ]

        for item in berkely_intro2:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")







def bentham(name):
    os.system('clear')

    bentham_intro=["You open the map again and start walking towards the next and FINAL destination",
                   "THE UTILITY STORE - says the map",
                   "Perfect, I can pick up some supplies for the battle! You think to yourself.",
                   "After walking for sometime you finally see the store and enter inside",
                   "",
                   "The store is nothing like you expected.",
                   "It shouldn't even be called a store you think to yourself.",
                   "It's simply a warehouse with signboards all over the walls.",
                   "PURITY, DURATION, CERTAINTY",
                   "What on earth is this? You think to yourself.",
                   "You walk over to the cashier",
                   "",
                   "Hello sir, I am "+name,
                   "The map brought me to this store. Might there be a stone here that I have to collect?.",
                   "",
                   "Strange Man : Finally, you have made it to me.",
                   "Strange Man : So tell me "+name,
                   "Strange Man : How many laws of utility have you kept in mind during your time here?",
                   "#####################",
                    "Option 1 : All of them, of course!",
                    "Option 2 : Laws Of utility?",
                   "Option 3 : None! I do what I want.",
                    "Type 1,2 or 3 to select.",
              "########################",
                   ""]

    for item in bentham_intro:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")


    answer1=input()

    while answer1 not in ['1','2','3']:
        prompt=["Please enter a valid input.",

                   "#####################",
                    "Option 1 : All of them, of course!",
                    "Option 2 : Laws Of utility?",
                   "Option 3 : None! I do what I want.",
                    "Type 1,2 or 3 to select.",
                    "########################",
                   ""]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer1=input()


    if answer1=="1":
        bentham_intro2=["Strange Man : Well if you did, then you must know who I am.",
                       "Strange Man : Tell me boy, who am I then?",
                       "################",
                        "Type the philosopher's last name.",
                       ""]

        for item in bentham_intro2:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer2=input()

        if answer2 not in ["Bentham","bentham","Jeremy Bentham","jeremy","Jeremy","BENTHAM","JEREMY"]:
            bentham_attitude1="bad"
            bentham_intro3=[
                "Of course I know who you are "+answer2,
                "Strange Man : Unbelievable. The saviour LIES!",
                       "Strange Man : I will give you ONE chance at redemption.",
            "Strange man : How many rules are there?",
            "################",
                "Type the number of rules of utility",
            ""]

            for item in bentham_intro3:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

            answer3= input()

            if answer3 not in ["7"]:
                bentham_attitude2="bad"
                bentham_intro3=[
                "Oh I know this! The number of rules are "+answer3,
                "Strange Man : AND HE LIES AGAIN!",
                       "Strange Man : Take the final stone and take your leave, we are hopeless after all.",""]

                for item in bentham_intro3:
                    for char in item:
                        sys.stdout.flush()
                        sys.stdout.write(char)
                        time.sleep(0.04)
                    print("")

            if answer3 == '7':
                bentham_attitude2="good"
                bentham_intro3=[
                "Oh I know this! The number of rules are "+answer3,
                "Strange Man : Good. If you don't know who I am, it doesn't matter as long as you had the rules in my mind.",
                       "Strange man : Will the prophecy be fulfilled after all? We shall see.",
                    ""]
                for item in bentham_intro3:
                    for char in item:
                        sys.stdout.flush()
                        sys.stdout.write(char)
                        time.sleep(0.04)
                    print("")


        if answer2 in ["Bentham","bentham","Jeremy Bentham","jeremy","Jeremy","BENTHAM","JEREMY"]:
            bentham_attitude1="good"

            bentham_intro3=[ "Of course I know who you are "+answer2,
                "Bentham : Utalitarian and honest, incredible!",
                       "Strange Man : Take the final stone and take your leave.",
            "Strange man : The prophecy will be fulfilled after all."]

            for item in bentham_intro3:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")


    if answer1=="2":
        bentham_attitude1="good"
        bentham_intro2=["Strange Man : Well, at least he is honest.",
                       "Strange Man : I am Bentham, the founder of the principle of utility",
                        "Bentham : I would be worried that you haven't been using the rules in your time here",
                        "Bentham : But I guess everyone has the rules at the back of their minds all the time anyway.",
                        "Strange Man : Take the final stone and take your leave.",
            "Strange man : Will the prophecy be fulfilled after all? We shall see.",
                       ""]

        for item in bentham_intro2:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")


    if answer1=="3":
        bentham_intro2=["Strange Man : HORRIBLE! DO YOU EVEN KNOW WHO I AM?",
                       "Of course I do! I am the saviour, you know",
                        "Strange Man: Tell me then.",
                       "################",
                        "Type the philosopher's last name.",
                       ""]

        for item in bentham_intro2:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer2=input()

        if answer2 not in ["Bentham","bentham","Jeremy Bentham","jeremy","Jeremy","BENTHAM","JEREMY"]:
            bentham_attitude1="bad"
            bentham_intro3=[
                "Of course I know who you are "+answer2,
                "Strange Man : Unbelievable. The saviour is a REBEL AND LIES!",
                       "Strange Man : I will give you ONE chance at redemption.",
            "Strange man : How many rules are there?",
            "################",
                "Type the number of rules of utility",
            ""]

            for item in bentham_intro3:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")

            answer3= input()

            if answer3 not in ["7"]:
                bentham_attitude3="bad"
                bentham_intro3=[
                "Oh I know this! The number of rules are "+answer3,
                "Strange Man : AND HE LIES AGAIN!",
                       "Strange Man : Take the final stone and take your leave, we are hopeless after all.",""]
                for item in bentham_intro3:
                    for char in item:
                        sys.stdout.flush()
                        sys.stdout.write(char)
                        time.sleep(0.01)
                    print("")

            if answer3 == '7':
                bentham_attitude3="good"
                bentham_intro3=[
                "Oh I know this! The number of rules are "+answer3,
                "Strange Man : Lucky guess. Take the stone.",
                       "Strange man : Will the prophecy be fulfilled after all? We shall see.",
                    ""]

                for item in bentham_intro3:
                    for char in item:
                        sys.stdout.flush()
                        sys.stdout.write(char)
                        time.sleep(0.04)
                    print("")



        if answer2 in ["Bentham","bentham","Jeremy Bentham","jeremy","Jeremy","BENTHAM","JEREMY"]:
            bentham_attitude2="good"

            bentham_intro3=[ "Of course I know who you are "+answer2,
                "Bentham : Lucky guess. I still have no hope.",
                       "Strange Man : Take the final stone and take your leave.",
            "Strange man : Who knows if the prophecy will be fulfilled after all."]

            for item in bentham_intro3:
                for char in item:
                    sys.stdout.flush()
                    sys.stdout.write(char)
                    time.sleep(0.04)
                print("")






def timothee(cat_attitude,name):
    os.system('clear')

    timothee_intro=["You place the stones together, to decipher the code",
                   "Decarte's stone : OEE",
                   "Berkeley's stone : TH",
                   "Bentham's stone : MIT",
                   "",
                   "O,E,E,T,H,M,I,T",
                   "",
                   "What could this possibly mean?!",
                   "#######################",
                   "Type the deciphered code : "]

    for item in timothee_intro:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

    answer1=input()

    while answer1 not in ["TIMOTHEE",'Timothee',"timothee"]:
        prompt=["That is the wrong cipher, try again.",
               "",
                   "O,E,E,T,H,M,I,T",
                   "",
                   "What could this possibly mean?!",
                   "#######################",
                   "Type the deciphered code : "]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        answer1=input()


    if answer1 in ["TIMOTHEE",'Timothee',"timothee"]:



        boss_battle=["T-t-TIMOTHEE?",
               "",
                "██░▀██████████████▀░██",
                "█▌▒▒░████████████░▒▒▐█",
                "█░▒▒▒░██████████░▒▒▒░█",
                "▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▐",
                "░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░",
                "███▀▀▀██▄▒▒▒▒▒▒▒▄██▀▀▀█",
                "██░░░▐█░▀█▒▒▒▒▒█▀░█▌░░░█",
                "▐▌░░░▐▄▌░▐▌▒▒▒▐▌░▐▄▌░░▐▌",
                "█░░░▐█▌░░▌▒▒▒▐░░▐█▌░░█",
                "▒▀▄▄▄█▄▄▄▌░▄░▐▄▄▄█▄▄▀▒",
                "░░░░░░░░░░└┴┘░░░░░░░░░",
                "██▄▄░░░░░░░░░░░░░░▄▄██",
                "████████▒▒▒▒▒▒████████",
                "█▀░░███▒▒░░▒░░▒▀██████",
                "█▒░███▒▒╖░░╥░░╓▒▐█████",
                "█▒░▀▀▀░░║░░║░░║░░█████",
                "██▄▄▄▄▀▀┴┴╚╧╧╝╧╧╝┴┴███",
                "██████████████████████"]




    for item in boss_battle:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.01)
        print("")


    boss_battle_final=["The Evil Demon...is...MY PROFESSOR'S CAT?",
                      "Timothee : meow",
                      "You can't be serious right now.",
                      "Timothee : meows louder",
                      "Well I mean, I could always give you some tuna?"]

    for item in boss_battle_final:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

    if cat_attitude=="bad":
        final_decision=["Here you go. Eat up","Timothee purrs in anger","Timothee screeches and attacks you","","WHAT THE HELL?! I'M LITERALLY GIVING YOU FOOD!","As he leaps over to attack you, you are rendered unconcious."]


    else:
        final_decision=["Oh shit! I gave the tuna to a kitten earlier. What do I do now?!",
                        "Timothee purrs in satisfaction",
                        "He comes closer, and lets you pet him",
                        "",
                        "Um, okay, well, here-here",
                        "He let's out the sweetest meow as you pet him",
                        "And you are rendered unconcious."]


    for item in final_decision:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

    next()

    os.system('clear')


    description = ["You wake up from what has felt like one of those naps that transform you into another dimension.",
                  "From your blurry vision, you see an old man crouching over you.",
                  "He seems to be examining you.",
                  "With glistening eyes and a wrinkly forehead, he finally says",
                   "",
                  "Old man : So, how was the game?",
                  "Game? What game? Where is Timothee?! Did I save the land?",
                  "Old man : Oh come on "+name,
                   "What? Did I finish the prophecy or not?!",
                   "Old man : How long are you going to pretend that you didn't just voluntarily subject yourself",
                    "Old man : To a series of obstacles, motivations, winning conditions",
                   "Old man : Completely submerged yourself",
                   "Old man : To a temporary agency?",
                   "Ngyuen?",
                   "Ngyuen: Ah see, you get it now.",
                   "Ngyuen: So tell me "+name,
                   "Ngyuen : Were you playing to strive, or to achieve?"
                   "",
                   "#######################",
                   "Option 1 : Strive",
                   "Option 2 : Achieve",
                   "Type 1 or 2 to choose your option.",
                   "#########################"

                  ]

    for item in description:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

    choice = input()



    while choice not in ["1",'2']:
        prompt=["Please enter a valid input",
               "",
                   "#######################",
                   "Option 1 : Strive",
                   "Option 2 : Achieve",
                   "Type 1 or 2 to choose your option.",
                   "#########################"]
        for item in prompt:
            for char in item:
                sys.stdout.flush()
                sys.stdout.write(char)
                time.sleep(0.04)
            print("")

        choice=input()

    if choice == "1":
        final=["Ngyuen : I see. Benjamin's course has taught you well.",
              "Ngyuen : My job here is done.",
              "Ngyuen : Hopefully we will see each other again, "+name]

    if choice == "2":
        final=["Ngyuen : I see. You haven't been paying attention in Benjamin's course.",
              "Ngyuen : Well then, I hope you play again, and I hope you play to strive.",
              "Ngyuen : We will see each other again, "+name]


    for item in final:
        for char in item:
            sys.stdout.flush()
            sys.stdout.write(char)
            time.sleep(0.04)
        print("")

        #go back to title screen



def play():
    name = intro()
    next()
    cat_attitude=cat()
    next()
    decartes_attitude2=decartes(name)
    next()
    berkely(decartes_attitude2,name)
    next()
    bentham(name)
    next()
    timothee(cat_attitude,name)
    next()
    main_screen()


def main_screen():
    import time
    import sys
    import os
    from os import system

    os.system('clear')


    os.system('clear')

    title_screen()

name = ""
cat_attitude=""
decartes_attitude2=""
main_screen()