#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import SpaceNinjaSystems

#master window
master = Tk()


labelFrame = Frame(master, width = 200, height = 100)
labelFrame.pack()

#topName has the fields for the first player
topNameFrame = Frame(master, width = 200, height = 100)
topNameFrame.pack()


#bottomName has the fields for the second player
bottomNameFrame = Frame(master, width = 200, height = 100)
bottomNameFrame.pack()

#button contains the go button to start the sim
buttonFrame = Frame(master, width = 200, height = 100)
buttonFrame.pack(fill=BOTH)


#labels of fields
#HPLabel = Label(labelFrame, text='HP')
#HPLabel.pack(side = RIGHT)
#defLabel = Label(labelFrame, text='Defend')
#defLabel.pack(side = RIGHT)
#attLabel = Label(labelFrame, text='Attack')
#attLabel.pack(side = RIGHT)
#temp instructions
tempLabel = Label(labelFrame, text='Please enter: Name/Attack/Defence/HP')
tempLabel.pack()

#name 1 for the first contestant
name1Label = Label(topNameFrame, text='Combatant 1:')
name1Label.pack(side = LEFT)
name1 = Entry(topNameFrame, bd =5)
name1.pack(side = LEFT)
attStat1 = Entry(topNameFrame, bd =5)
attStat1.pack(side = LEFT)
defStat1 = Entry(topNameFrame, bd =5)
defStat1.pack(side = LEFT)
hpStat1 = Entry(topNameFrame, bd = 5)
hpStat1.pack(side = LEFT)

#name 2 for the second contestant
name2Label = Label(bottomNameFrame, text='Combatant 2:')
name2Label.pack(side = LEFT)
name2 = Entry(bottomNameFrame, bd =5)
name2.pack(side = LEFT)
attStat2 = Entry(bottomNameFrame, bd =5)
attStat2.pack(side = LEFT)
defStat2 = Entry(bottomNameFrame, bd =5)
defStat2.pack(side = LEFT)
hpStat2 = Entry(bottomNameFrame, bd = 5)
hpStat2.pack(side = LEFT)


#bugs are the worst
name1.insert(0,"Name")
attStat1.insert(0,"Attack")
defStat1.insert(0,"Defence")
hpStat1.insert(0,"Hit Points")
name2.insert(0,"Name")
attStat2.insert(0,"Attack")
defStat2.insert(0,"Defence")
hpStat2.insert(0,"Hit Points")




def fight(SpaceNinjaWizard1, SpaceNinjaWizard2):
    #face off and collect data about 2 spaceNinjaWizards
    wins = 0
    draws = 0
    loss = 0
    noIterations = 1000
    for i in range(noIterations):
        spaceNinja1 = SpaceNinjaSystems.SpaceNinja(SpaceNinjaWizard1.hp,SpaceNinjaWizard1.att,SpaceNinjaWizard1.defence,SpaceNinjaWizard1.crit,0,SpaceNinjaWizard1.styleName)
        spaceNinja2 = SpaceNinjaSystems.SpaceNinja(SpaceNinjaWizard2.hp,SpaceNinjaWizard2.att,SpaceNinjaWizard2.defence,SpaceNinjaWizard2.crit,0,SpaceNinjaWizard2.styleName)
        result = SpaceNinjaSystems.fight(spaceNinja1, spaceNinja2)
        if result == 1:
            wins += 1
        elif result == 2:
            loss += 1
        elif result == 0:
            draws += 1
    #display the results in a nice window
    readableWins = wins/float(noIterations) *100
    readableLoss = loss/float(noIterations) *100
    readableDraw = draws/float(noIterations) * 100

    tkMessageBox.showinfo( "you played a game!", SpaceNinjaWizard1.styleName + " wins = " + str(readableWins) + "% of the time.\n"+
                           SpaceNinjaWizard2.styleName + " wins = " + str(readableLoss) + "% of the time,\n"+
                           "and the match draws: " + str(readableDraw) + "% of the time")

def Analyze():
    #collect stat data
    #names can stay as strings


    #verify all that should be number are and assign
    try:
        firstAttStat = int(attStat1.get())
    except ValueError:
        tkMessageBox.showinfo( "Error", "The First combatants Attack stat is invalid")
        return
    try:
        firstDefStat = int(defStat1.get())
    except ValueError:
        tkMessageBox.showinfo( "Error", "The First combatants Defence stat is invalid")
        return
    try:
        print(hpStat1.get())
        firstHp = int(hpStat1.get())
    except ValueError:
        tkMessageBox.showinfo( "Error", "The First combatants Hp stat is invalid")
        return
    try:
        secondAttStat = int(attStat2.get())
    except ValueError:
        tkMessageBox.showinfo( "Error", "The Seccond combatants Attack stat is invalid")
        return
    try:
        secondDefStat = int(defStat2.get())
    except ValueError:
        tkMessageBox.showinfo( "Error", "The Second combatants Defence stat is invalid")
        return
    try:
        secondHp = int(hpStat2.get())
    except ValueError:
        tkMessageBox.showinfo( "Error", "The Second combatants Hp stat is invalid")
        return
    firstName = name1.get()
    secondName = name2.get()
    
    #lets make some SpaceNinjas!
    player1 = SpaceNinjaSystems.SpaceNinja(firstHp,firstAttStat,firstDefStat,20,0,firstName)
    player2 = SpaceNinjaSystems.SpaceNinja(secondHp,secondAttStat,secondDefStat,20,0,secondName)
    #player1 = SpaceNinjaSystems.SpaceNinja(0,0,0,20,0,firstName)
    #player2 = SpaceNinjaSystems.SpaceNinja(0,0,0,20,0,secondName)
    
    #call fight
    fight(player1,player2)

activateButton = Button(buttonFrame, text = 'Analyze', command = Analyze)
activateButton.pack(side = RIGHT)

#make the button call something
#checks that the data entered is valid
#assembles 2x spaceNinjas
#does a big loop of fights,
#displays the results in a not shit results window


master.mainloop()
