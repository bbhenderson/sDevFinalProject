from breezypythongui import EasyFrame



class ColonyCraftMain(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, background='#47FFF3', title="Welcome to Colony Craft")
        self.addLabel(text="Welcome to Colony Craft: ", row=0, column=0, columnspan=3, sticky="NESW")
        self.addLabel(text="Click a button below to begin. ", row=1, column=0, columnspan=3, sticky="NESW")

        self.globalPlayersDict = self.globalPlayersDict = {
            1: {'playerNumber': 1, 'name': 'Amanda', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            2: {'playerNumber': 2, 'name': 'Brittany', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            3: {'playerNumber': 3, 'name': 'Charlie', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            4: {'playerNumber': 4, 'name': 'David', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            5: {'playerNumber': 5, 'name': 'Elizabeth', 'points': 0, 'team': 'Cobras', 'teamNumber': 3},
            6: {'playerNumber': 6, 'name': 'Frank', 'points': 0, 'team': 'Cobras', 'teamNumber': 3}}
        self.teamsDict = self.teamsDict = {1: {'teamNumber': 1, 'teamName': 'Anacondas'},
                                           2: {'teamNumber': 2, 'teamName': 'Boas'},
                                           3: {'teamNumber': 3, 'teamName': 'Cobras'}}
        self.eventsDict = self.eventsDict = {
            1: {'eventNumber': 1, 'description': "You make a successful trade with the native people",
                'effect': 'positive',
                'pointChange': +150, 'appliesTo': 'player'},
            2: {'eventNumber': 2, 'description': "Your crops produces a good harvest. Your team eats well.",
                'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
            3: {'eventNumber': 3, 'description': "You find a plant to cure illness. Your whole team feels better.",
                'effect': 'positive', 'pointChange': +200, 'appliesTo': 'team'},
            4: {'eventNumber': 4, 'description': "You install a Franklin stove to keep warm", 'effect': 'positive',
                'pointChange': +150, 'appliesTo': 'player'},
            5: {'eventNumber': 5, 'description': "You receive a letter from back home.", 'effect': 'positive',
                'pointChange': +300, 'appliesTo': 'player'},
            6: {'eventNumber': 6, 'description': "The winter is long and hard. Your team struggles",
                'effect': 'negative',
                'pointChange': -200, 'appliesTo': 'team'},
            7: {'eventNumber': 7, 'description': "You eat an unknown plant and fall ill.", 'effect': 'negative',
                'pointChange': -150, 'appliesTo': 'player'},
            8: {'eventNumber': 8, 'description': "Pirates attack your merchant ship. Your team's supplies are stolen.",
                'effect': 'negative', 'pointChange': -300, 'appliesTo': 'team'},
            9: {'eventNumber': 9, 'description': "Other colonists attack your settlement at night.",
                'effect': 'negative',
                'pointChange': -200, 'appliesTo': 'team'},
            10: {'eventNumber': 10, 'description': "You drink tainted water and fall ill.", 'effect': 'negative',
                 'pointChange': -150, 'appliesTo': 'player'},
            11: {'eventNumber': 11, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
                 'pointChange': +0, 'appliesTo': 'player'},
            12: {'eventNumber': 12, 'description': "Today was boring. Nothing happened.", 'effect': 'neutral',
                 'pointChange': +0, 'appliesTo': 'player'}}

        self.attendanceBtn = self.addButton(text="Attendance", row=2, column=0, command=self.attendance_window())
        self.randomEventBtn = self.addButton(text="Random Event", row=2, column=1)
        self.leaderboardBtn = self.addButton(text="Leaderboard", row=2, column=2)

    def attendance_window(self):
        window = Attendance()
        window.grab_set()
        #for i in globalPlayersDict:
            #print("Is", globalPlayersDict[i].get('name'), " here? ")
            #isHere = input("Enter Y for y; N for no.")
            #if isHere.lower() == 'y': globalPlayersDict[i]['points'] += 20


class Attendance(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, background='#47FFF3', title="Attendance")
        self.globalPlayersDict = self.globalPlayersDict = {
            1: {'playerNumber': 1, 'name': 'Amanda', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            2: {'playerNumber': 2, 'name': 'Brittany', 'points': 0, 'team': 'Anacondas', 'teamNumber': 1},
            3: {'playerNumber': 3, 'name': 'Charlie', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            4: {'playerNumber': 4, 'name': 'David', 'points': 0, 'team': 'Boas', 'teamNumber': 2},
            5: {'playerNumber': 5, 'name': 'Elizabeth', 'points': 0, 'team': 'Cobras', 'teamNumber': 3},
            6: {'playerNumber': 6, 'name': 'Frank', 'points': 0, 'team': 'Cobras', 'teamNumber': 3}}
        self.addLabel(text="Attendance: ", row=0, column=0, sticky="NESW")
        self.addLabel(text="Here", row=1, column=1, sticky="NESW")
        self.addLabel(text="Absent", row=1, column=2, sticky="NESW")
        for i in self.globalPlayersDict:
            self.addLabel(text=self.globalPlayersDict[i], row=2, column=0, sticky="NESW")
            self.addRadioButton("Here")
            self.addRadioButton("Absent")








    def random_event(self, globalPlayersDict, teamsDict, eventsDict):
        import random
        randomEventNumber = random.randint(1, len(eventsDict))
        print("Today's Random Event:")
        print("This Random Event is for: ")


        ##If event is for random player:
        if eventsDict[randomEventNumber].get('appliesTo') == 'player':
            randomPlayerNumber = random.randint(1, len(globalPlayersDict))
            print(globalPlayersDict[randomPlayerNumber].get('name'))
            globalPlayersDict[randomPlayerNumber]['points'] += eventsDict[randomEventNumber].get('pointChange')


        # If event is for random team:
        if eventsDict[randomEventNumber].get('appliesTo') == 'team':
            randomTeamNumber = random.randint(1, len(teamsDict))
            affectedTeam = teamsDict[randomTeamNumber].get('teamName')
            print(affectedTeam)
            for i in globalPlayersDict.keys():
                # print(d.keys())
                for k, v in globalPlayersDict.items():
                    if v['team'] == affectedTeam:
                        globalPlayersDict[k]['points'] += eventsDict[randomEventNumber].get('pointChange')
        # Print event and effect:
        print(eventsDict[randomEventNumber].get('description'))
        if eventsDict[randomEventNumber].get('effect') == 'positive':
            print("You gain ", eventsDict[randomEventNumber].get('pointChange'), " points!")

        elif eventsDict[randomEventNumber].get('effect') == 'negative':
            print("You lose ", eventsDict[randomEventNumber].get('pointChange'), " points!")

        # Print affected player names with new points here
        return globalPlayersDict


    def leaderboard(self, globalPlayersDict):
        print("Under Construction.")



def main():
    ColonyCraftMain().mainloop()

if __name__ == "__main__":
    main()