#!/usr/bin/env python
# coding: utf-8

# In[159]:


from tkinter import * 
from PIL import ImageTk,Image

globalPlayersDict = {
            1: {'playerNumber': 1, 'name': 'Amanda', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            2: {'playerNumber': 2, 'name': 'Brittany', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            3: {'playerNumber': 3, 'name': 'Charlie', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            4: {'playerNumber': 4, 'name': 'David', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            5: {'playerNumber': 5, 'name': 'Elizabeth', 'points': 0, 'team': 'Cobras', 'teamNumber': 3},
            6: {'playerNumber': 6, 'name': 'Frank', 'points': 0, 'team': 'Cobras', 'teamNumber': 3}} # Dictionary with Demo Players

eventsDict = {
    1: {'eventnumber': 1, 'description': "You make a successful trade with the native people",
        'effect': 'positive',
        'pointChange': +150, 'appliesTo': 'player'},
    2: {'eventnumber': 2, 'description': "Your crops produce a good harvest. Your team eats well.",
        'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
    3: {'eventnumber': 3, 'description': "You find a plant to cure illness. Your whole team feels better.",
        'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
    4: {'eventnumber': 4, 'description': "You install a Franklin stove to keep warm", 'effect': 'positive',
        'pointChange': +150, 'appliesTo': 'player'},
    5: {'eventnumber': 5, 'description': "You receive a letter from back home.", 'effect': 'positive',
        'pointChange': +300, 'appliesTo': 'player'},
    6: {'eventnumber': 6, 'description': "The winter is long and hard. Your team struggles",
        'effect': 'negative',
        'pointChange': -200, 'appliesTo': 'team'},
    7: {'eventnumber': 7, 'description': "You eat an unknown plant and fall ill.", 'effect': 'negative',
        'pointChange': -150, 'appliesTo': 'player'},
    8: {'eventnumber': 8, 'description': "Pirates attack your merchant ship. Your team's supplies are stolen.",
        'effect': 'negative', 'pointChange': -300, 'appliesTo': 'team'},
    9: {'eventnumber': 9, 'description': "Other colonists attack your settlement at night.",
        'effect': 'negative',
        'pointChange': -200, 'appliesTo': 'team'},
    10: {'eventnumber': 10, 'description': "You drink tainted water and fall ill.", 'effect': 'negative',
         'pointChange': -150, 'appliesTo': 'player'},
    11: {'eventnumber': 11, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
         'pointChange': +0, 'appliesTo': 'player'},
    12: {'eventnumber': 12, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
         'pointChange': +0, 'appliesTo': 'player'}} # Dictionary with random event descriptions, points to be added or taken away, and who the even applies to (team or person)

teamsDict = {1: {'teamNumber': 1, 'teamName': 'Anacondas'},
                                           2: {'teamNumber': 2, 'teamName': 'Boas'},
                                           3: {'teamNumber': 3, 'teamName': 'Cobras'}}#Dictionary holding demo team names




def attendance_window():
    """"Creates the attendance window, to be opened by the “Attendance” button on the root window"""""
    top = Toplevel()
    label = Label(top, text="Attendance").grid(row=0, column=0, columnspan=3)
    hereLabel = Label(top, text="Here?"). grid(row=1, column=1)
    backButton = Button(top, text="Back", command=top.destroy).grid(row=10, column=5)
    here=IntVar()
    here.get()
    submitButton = Button(top, text="Submit", command=submit()).grid(row=9, column = 5)
    
    def submit():
        hereDict = {}
        for x in range(len(globalPlayersDict)):
            if here.get() ==1:
                hereDict["{0}".format(x+1)] = 1
            else:
                hereDict["{0}".format(x+1)] = 0
            print(hereDict)
 #   for i in globalPlayersDict:
  #      here.get()
   #     if here.get() == 1:
    #        globalPlayersDict[i]['points'] += 20
    

    #For each entry in the gloablPlayersDict Dictionary, a label is created with the player’s name and a check box indicating if they are present at school that day. When checked, the box will award 20 points (to be changed in the globalPlayersDict ‘points’ key). No change for absent students”
    for i in globalPlayersDict:
        playerNamesLabel= Label(top, text=globalPlayersDict[i].get('name')).grid(row=i+1, column=0)#creates a new label for each player in the dictionary
        here=IntVar()
        here.get()
        check=Checkbutton(top, variable=hereDict[i]).grid(row=i+1, column=1)
        hereValueLabel= Label(top, text= "Here?").grid (row=i+1, column=2)
        submitButton = Button(top, text="Submit", command= submit)
        
        
def random_event_window():
    """"Creates the random event window, to be opened by the “Random Event” button on the root window"""""
    top = Toplevel()
    label = Label(top, text="Random Event").grid(row=0, column=0)
    backButton= Button(top, text="Back", command=top.destroy).grid(row=10, column=5)

    
def leader_board_window():
    """"Creates the leaderboard window, to be opened by the “Leader Board” button on the root window"""""
    top = Toplevel()
    label = Label(top, text="Leader Board").grid(row=0, column=0)
    backButton= Button(top, text="Back", command=top.destroy).grid(row=10, column=5)    

#creates the main window, which is launched when the program runs. Includes buttons to the other windows (attendance, random event and leaderboard) and a quit button.
root = Tk()
label = Label (root, text = "Welcome to Colony Craft-- Demo"). grid(row=0, column=1, columnspan=3)
tCooke = ImageTk.PhotoImage(Image.open("Pictures/tCooke.png")) #image of the Thomas Cooke character from the game
tCookeLabel = Label(image=tCooke).grid(row=0, column=0, rowspan=2)
attendanceBtn = Button(root, text="Attendance", command=attendance_window).grid(row=1, column=1)
randomEventBtn = Button(root, text="Random Event", command=random_event_window).grid(row=1, column=2)
LeaderBoardBtn = Button(root, text="Leader Board", command=leader_board_window).grid(row=1, column=3)
quitBtn = Button(root, text="Quit", padx=30, command=root.destroy).grid(row=21, column=3)




mainloop()
print(globalPlayersDict)


# In[47]:


from tkinter import * 
from PIL import ImageTk,Image
import random

globalPlayersDict = {
            1: {'playerNumber': 1, 'name': 'Amanda', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            2: {'playerNumber': 2, 'name': 'Brittany', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            3: {'playerNumber': 3, 'name': 'Charlie', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            4: {'playerNumber': 4, 'name': 'David', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            5: {'playerNumber': 5, 'name': 'Elizabeth', 'points': 0, 'team': 'Cobras', 'teamNumber': 3},
            6: {'playerNumber': 6, 'name': 'Frank', 'points': 0, 'team': 'Cobras', 'teamNumber': 3}} # Dictionary with Demo Players

eventsDict = {
    1: {'eventnumber': 1, 'description': "You make a successful trade with the native people",
        'effect': 'positive',
        'pointChange': +150, 'appliesTo': 'player'},
    2: {'eventnumber': 2, 'description': "Your crops produce a good harvest. Your team eats well.",
        'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
    3: {'eventnumber': 3, 'description': "You find a plant to cure illness. Your whole team feels better.",
        'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
    4: {'eventnumber': 4, 'description': "You install a Franklin stove to keep warm", 'effect': 'positive',
        'pointChange': +150, 'appliesTo': 'player'},
    5: {'eventnumber': 5, 'description': "You receive a letter from back home.", 'effect': 'positive',
        'pointChange': +300, 'appliesTo': 'player'},
    6: {'eventnumber': 6, 'description': "The winter is long and hard. Your team struggles",
        'effect': 'negative',
        'pointChange': -200, 'appliesTo': 'team'},
    7: {'eventnumber': 7, 'description': "You eat an unknown plant and fall ill.", 'effect': 'negative',
        'pointChange': -150, 'appliesTo': 'player'},
    8: {'eventnumber': 8, 'description': "Pirates attack your merchant ship. Your team's supplies are stolen.",
        'effect': 'negative', 'pointChange': -300, 'appliesTo': 'team'},
    9: {'eventnumber': 9, 'description': "Other colonists attack your settlement at night.",
        'effect': 'negative',
        'pointChange': -200, 'appliesTo': 'team'},
    10: {'eventnumber': 10, 'description': "You drink tainted water and fall ill.", 'effect': 'negative',
         'pointChange': -150, 'appliesTo': 'player'},
    11: {'eventnumber': 11, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
         'pointChange': +0, 'appliesTo': 'player'},
    12: {'eventnumber': 12, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
         'pointChange': +0, 'appliesTo': 'player'}} # Dictionary with random event descriptions, points to be added or taken away, and who the even applies to (team or person)

teamsDict = {1: {'teamNumber': 1, 'teamName': 'Anacondas'},
                                           2: {'teamNumber': 2, 'teamName': 'Boas'},
                                           3: {'teamNumber': 3, 'teamName': 'Cobras'}}#Dictionary holding demo team names
hereDict=[]
def attendance_window():
    """"Creates the attendance window, to be opened by the “Attendance” button on the root window"""
    top = Toplevel()
    label = Label(top, text="Attendance", font=("Arial", 20)).grid(row=0, column=0, columnspan=3)
    hereLabel= Label(top, text="Here?",font=("Arial", 13)). grid(row=1, column=1)
    backButton= Button(top, text="Back", command=top.destroy).grid(row=18, column=5)
   
    
    def submit():
        for i, value in enumerate(hereDict):
            here.get()
            hereValueLabel= Label(top, text=here.get(),font=("Arial", 14)).grid (row=(i+(i+3)), column=2)
            for i, value in enumerate(hereDict):
                if hereDict[i] ==1:
                    globalPlayersDict[i]['points'] += 20

    submitButton= Button(top, text="Submit", command=submit).grid(row=16, column=5)
    
    #For each entry in the gloablPlayersDict Dictionary, a label is created with the player’s name and a check box indicating if they are present at school that day. When checked, the box will award 20 points (to be changed in the globalPlayersDict ‘points’ key). No change for absent students”
    for i in globalPlayersDict:
        playerNamesLabel= Label(top, text=globalPlayersDict[i].get('name') , font=("Arial", 14)).grid(row=(i+(i+1)), column=0)#creates a new label for each player in the dictionary
        here=IntVar()
        check=Checkbutton(top, variable=here).grid(row=(i+(i+1)), column=1)
        emptySpace7= Label(top, text="", font=("Arial", 12)).grid(row=(i+(i+2)), column=0, columnspan=5)
        hereDict.append(here)
        
        
    
    
def random_event_window():
    """"Creates the random event window, to be opened by the “Random Event” button on the root window"""
    top = Toplevel()
    label = Label(top, text="Random Event", font=("Arial", 20)).grid(row=0, column=0, columnspan=5)
    backButton= Button(top, text="Back", command=top.destroy).grid(row=13, column=5)
    emptySpace1= Label(top, text="", font=("Arial", 12)).grid(row=1, column=0, columnspan=5)
    emptySpace2= Label(top, text="", font=("Arial", 12)).grid(row=3, column=0, columnspan=5)
    emptySpace3= Label(top, text="", font=("Arial", 12)).grid(row=5, column=0, columnspan=5, rowspan=2)
    emptySpace4= Label(top, text="", font=("Arial", 12)).grid(row=8, column=0, columnspan=5)
    emptySpace5= Label(top, text="", font=("Arial", 12)).grid(row=10, column=0, columnspan=5)
    def random_event():

        randomEventNumber = random.randint(1, len(eventsDict))
        
        randomEventLabel= Label(top, text="Today's Random Event:", font=("Arial", 13)). grid(row=2, column=0, columnspan=5)
        applestoLabel=Label(top, text="This Random Event is for: ", font=("Arial", 13)).grid(row=7, column=0, columnspan=5)


        ##If event is for random player:
        if eventsDict[randomEventNumber].get('appliesTo') == 'player':
            randomPlayerNumber = random.randint(1, len(globalPlayersDict))
            randomPlayerLabel= Label(top, text=globalPlayersDict[randomPlayerNumber].get('name'), 
                                     font=("Arial", 20)).grid(row=9, column=0, columnspan=5)
            globalPlayersDict[randomPlayerNumber]['points'] += eventsDict[randomEventNumber].get('pointChange')


        # If event is for random team:
        if eventsDict[randomEventNumber].get('appliesTo') == 'team':
            randomTeamNumber = random.randint(1, len(teamsDict)) #random number used to select affected team
            affectedTeam = teamsDict[randomTeamNumber].get('teamName')
            randomTeamLable= Label(top, text="The " + affectedTeam , font=("Arial", 20)).grid(row=9, column=0, columnspan=5)
        
            for k, v in globalPlayersDict.items():
                if v['team'] == affectedTeam:
                    globalPlayersDict[k]['points'] += eventsDict[randomEventNumber].get('pointChange')
                else:
                    globalPlayersDict[k]['points'] += 0
        # Print event and effect:
        randomEventLabel=Label(top, text=eventsDict[randomEventNumber].get('description'), font=
                               ("Arial", 15)).grid(row=4, column=0, columnspan=5)
        if eventsDict[randomEventNumber].get('effect') == 'positive':
            gainLabel= Label(top, text="You gain "+ str(eventsDict[randomEventNumber].get('pointChange'))+ 
                             " points!", font=("Arial", 13)).grid(row=11, column=0, columnspan=5)

        elif eventsDict[randomEventNumber].get('effect') == 'negative':
            loseLabel= Label(top, text="You lose "+ str(eventsDict[randomEventNumber].get('pointChange'))+ 
                             " points!", font=("Arial", 13)).grid(row=11, column=0, columnspan=5)

        # Print affected player names with new points here
        return globalPlayersDict
    
    random_event()
    
    
def leader_board_window():
    """Creates the leaderboard window, to be opened by the “Leader Board” button on the root window"""
    top = Toplevel()
    leaderBoardLabel = Label(top, text="Leader Board", font=("Arial", 20)).grid(row=0, column=0, columnspan=5)
    backButton= Button(top, text="Back", command=top.destroy).grid(row=10, column=5)   
   
# for some reason the labels appear as an alphabetized list, but the print function works fine
    your_dict = dict(sorted(globalPlayersDict.items(), key = lambda x: (x[1]["points"], x[1]["name"]), reverse=True))
    for i in your_dict:
        print(your_dict[i]['name'], your_dict[i]['points'])
        leaderBoardNameLabel= Label(top, text= str(your_dict[i]['name']), font=("Arial", 13)).grid(row=i+1, column=0, sticky=W)
        leaderBoardPointLabel= Label(top, text=str(your_dict[i]['points']), font=("Arial", 13)).grid(row=i+1, column=1, sticky=E)
        
    
    

#creates the main window, which is launched when the program runs. Includes buttons to the other windows (attendance, random event and leaderboard) and a quit button.
root = Tk()
root.title("Colony Craft")
label = Label (root, text = "Welcome to Colony Craft: \nDemo", font=("Arial", 20)). grid(row=0, column=1, columnspan=3)
tCooke = ImageTk.PhotoImage(Image.open("Pictures/tCooke.png")) #image of the Thomas Cooke character from the game
tCookeLabel = Label(image=tCooke).grid(row=0, column=0, rowspan=2)
attendanceBtn = Button(root, text="Attendance", command=attendance_window).grid(row=1, column=1)
randomEventBtn = Button(root, text="Random Event", command=random_event_window).grid(row=1, column=2)
LeaderBoardBtn = Button(root, text="Leader Board", command=leader_board_window).grid(row=1, column=3)
quitBtn = Button(root, text="Quit", padx=30, command=root.destroy).grid(row=21, column=3)




mainloop()



# In[20]:


from tkinter import *
from PIL import ImageTk, Image
import random

globalPlayersDict = {
    1: {'playerNumber': 1, 'name': 'Amanda', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
    2: {'playerNumber': 2, 'name': 'Brittany', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
    3: {'playerNumber': 3, 'name': 'Charlie', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
    4: {'playerNumber': 4, 'name': 'David', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
    5: {'playerNumber': 5, 'name': 'Elizabeth', 'points': 0, 'team': 'Cobras', 'teamNumber': 3},
    6: {'playerNumber': 6, 'name': 'Frank', 'points': 0, 'team': 'Cobras',
        'teamNumber': 3}}  # Dictionary with Demo Players

eventsDict = {
    1: {'eventnumber': 1, 'description': "You make a successful trade with the native people",
        'effect': 'positive',
        'pointChange': +150, 'appliesTo': 'player'},
    2: {'eventnumber': 2, 'description': "Your crops produce a good harvest. Your team eats well.",
        'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
    3: {'eventnumber': 3, 'description': "You find a plant to cure illness. Your whole team feels better.",
        'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
    4: {'eventnumber': 4, 'description': "You install a Franklin stove to keep warm", 'effect': 'positive',
        'pointChange': +150, 'appliesTo': 'player'},
    5: {'eventnumber': 5, 'description': "You receive a letter from back home.", 'effect': 'positive',
        'pointChange': +300, 'appliesTo': 'player'},
    6: {'eventnumber': 6, 'description': "The winter is long and hard. Your team struggles",
        'effect': 'negative',
        'pointChange': -200, 'appliesTo': 'team'},
    7: {'eventnumber': 7, 'description': "You eat an unknown plant and fall ill.", 'effect': 'negative',
        'pointChange': -150, 'appliesTo': 'player'},
    8: {'eventnumber': 8, 'description': "Pirates attack your merchant ship. Your team's supplies are stolen.",
        'effect': 'negative', 'pointChange': -300, 'appliesTo': 'team'},
    9: {'eventnumber': 9, 'description': "Other colonists attack your settlement at night.",
        'effect': 'negative',
        'pointChange': -200, 'appliesTo': 'team'},
    10: {'eventnumber': 10, 'description': "You drink tainted water and fall ill.", 'effect': 'negative',
         'pointChange': -150, 'appliesTo': 'player'},
    11: {'eventnumber': 11, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
         'pointChange': +0, 'appliesTo': 'player'},
    12: {'eventnumber': 12, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
         'pointChange': +0,
         'appliesTo': 'player'}}  # Dictionary with random event descriptions, points to be added or taken away, 
# and who the even applies to (team or person) 

teamsDict = {1: {'teamNumber': 1, 'teamName': 'Anacondas'},
             2: {'teamNumber': 2, 'teamName': 'Boas'},
             3: {'teamNumber': 3, 'teamName': 'Cobras'}}  # Dictionary holding demo team names
hereDict = []


#def attendance_window():
   # """"Creates the attendance window, to be opened by the “Attendance” button on the root window"""
    #top = Toplevel()
   #label = Label(top, text="Attendance", font=("Arial", 20)).grid(row=0, column=0, columnspan=3)
    #hereLabel = Label(top, text="Here?", font=("Arial", 13)).grid(row=1, column=1)
   # backButton = Button(top, text="Back", command=top.destroy).grid(row=18, column=5)

    #def submit():

        #hereDict.append(here)
        #for j in hereDict:
            #hereValueLabel = Label(top, text=str(hereDict[int(j)]), font=("Arial", 14)).grid(row=(i + (i + 3)), column=2)
            #for k in hereDict:
                #if hereDict[k] == 1:
                    #globalPlayersDict[k]['points'] += 20

    #submitButton = Button(top, text="Submit", command=submit).grid(row=16, column=5)

    # For each entry in the globalPlayersDict Dictionary, a label is created with the player’s name and a check box 
    # indicating if they are present at school that day. When checked, the box will award 20 points (to be changed in
    # the globalPlayersDict ‘points’ key). No change for absent students” 
    #for i in globalPlayersDict:
       # here = IntVar()
       # playerNamesLabel = Label(top, text=globalPlayersDict[i].get('name'), font=("Arial", 14)).grid(row=(i + (i + 1)),
                                                                                                      #column=0)  # creates a new label for each player in the dictionary
        #check = Checkbutton(top, variable=here).grid(row=(i + (i + 1)), column=1)
       # emptySpace7 = Label(top, text="", font=("Arial", 12)).grid(row=(i + (i + 2)), column=0, columnspan=5)


def random_event_window():
    """"Creates the random event window, to be opened by the “Random Event” button on the root window"""
    top = Toplevel()
    label = Label(top, text="Random Event", font=("Arial", 20)).grid(row=0, column=0, columnspan=5)
    backButton = Button(top, text="Back", command=top.destroy).grid(row=13, column=5)
    emptySpace1 = Label(top, text="", font=("Arial", 12)).grid(row=1, column=0, columnspan=5)
    emptySpace2 = Label(top, text="", font=("Arial", 12)).grid(row=3, column=0, columnspan=5)
    emptySpace3 = Label(top, text="", font=("Arial", 12)).grid(row=5, column=0, columnspan=5, rowspan=2)
    emptySpace4 = Label(top, text="", font=("Arial", 12)).grid(row=8, column=0, columnspan=5)
    emptySpace5 = Label(top, text="", font=("Arial", 12)).grid(row=10, column=0, columnspan=5)

    def random_event():

        randomEventNumber = random.randint(1, len(eventsDict))

        randomEventLabel = Label(top, text="Today's Random Event:", font=("Arial", 13)).grid(row=2, column=0,
                                                                                             columnspan=5)
        appliestoLabel = Label(top, text="This Random Event is for: ", font=("Arial", 13)).grid(row=7, column=0,
                                                                                               columnspan=5)

        ##If event is for random player:
        if eventsDict[randomEventNumber].get('appliesTo') == 'player':
            randomPlayerNumber = random.randint(1, len(globalPlayersDict))
            randomPlayerLabel = Label(top, text=globalPlayersDict[randomPlayerNumber].get('name'),
                                      font=("Arial", 20)).grid(row=9, column=0, columnspan=5)
            globalPlayersDict[randomPlayerNumber]['points'] += eventsDict[randomEventNumber].get('pointChange')

        # If event is for random team:
        if eventsDict[randomEventNumber].get('appliesTo') == 'team':
            randomTeamNumber = random.randint(1, len(teamsDict))  # random number used to select affected team
            affectedTeam = teamsDict[randomTeamNumber].get('teamName')
            randomTeamLabel = Label(top, text="The " + affectedTeam, font=("Arial", 20)).grid(row=9, column=0,
                                                                                              columnspan=5)

            for k, v in globalPlayersDict.items():
                if v['team'] == affectedTeam:
                    globalPlayersDict[k]['points'] += eventsDict[randomEventNumber].get('pointChange')
                else:
                    globalPlayersDict[k]['points'] += 0
        # Print event and effect:
        randomEventLabel = Label(top, text=eventsDict[randomEventNumber].get('description'), font=
        ("Arial", 15)).grid(row=4, column=0, columnspan=5)
        if eventsDict[randomEventNumber].get('effect') == 'positive':
            gainLabel = Label(top, text="You gain " + str(eventsDict[randomEventNumber].get('pointChange')) +
                                        " points!", font=("Arial", 13)).grid(row=11, column=0, columnspan=5)

        elif eventsDict[randomEventNumber].get('effect') == 'negative':
            loseLabel = Label(top, text="You lose " + str(eventsDict[randomEventNumber].get('pointChange')) +
                                        " points!", font=("Arial", 13)).grid(row=11, column=0, columnspan=5)

        # Print affected player names with new points here
        return globalPlayersDict

    random_event()


def leader_board_window():
    """Creates the leaderboard window, to be opened by the “Leader Board” button on the root window"""
    top = Toplevel()
    leaderBoardLabel = Label(top, text="Leader Board", font=("Arial", 20)).grid(row=0, column=0, columnspan=5)
    backButton = Button(top, text="Back", command=top.destroy).grid(row=10, column=5)

    # for some reason the labels appear as an alphabetized list, but the print function works fine
    your_dict = dict(sorted(globalPlayersDict.items(), key=lambda x: (x[1]["points"], x[1]["name"]), reverse=True))
    for i in your_dict:
        #print(your_dict[i]['name'], your_dict[i]['points'])
        leaderBoardNameLabel = Label(top, text=str(your_dict[i]['name']), font=("Arial", 13)).grid(row=i + 1, column=0,
                                                                                                   sticky=W)
        leaderBoardPointLabel = Label(top, text=str(your_dict[i]['points']), font=("Arial", 13)).grid(row=i + 1,
                                                                                                      column=1,
                                                                                                      sticky=E)


# creates the main window, which is launched when the program runs. Includes buttons to the other windows (attendance, random event and leaderboard) and a quit button.
root = Tk()
root.title("Colony Craft")
label = Label(root, text="Welcome to Colony Craft: \nDemo", font=("Arial", 20)).grid(row=0, column=1, columnspan=3)
tCooke = ImageTk.PhotoImage(Image.open("Pictures/tCooke.png"))  # image of the Thomas Cooke character from the game
tCookeLabel = Label(image=tCooke).grid(row=0, column=0, rowspan=2)
#attendanceBtn = Button(root, text="Attendance", command=attendance_window).grid(row=1, column=1)
randomEventBtn = Button(root, text="Random Event", command=random_event_window).grid(row=1, column=2)
LeaderBoardBtn = Button(root, text="Leader Board", command=leader_board_window).grid(row=1, column=3)
quitBtn = Button(root, text="Quit", padx=30, command=root.destroy).grid(row=21, column=3)

mainloop()







# In[ ]:




