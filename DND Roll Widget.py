from tkinter import *
root = Tk()
root.title("DND Roll Widget")
root.geometry("750x450")
#root.configure(bg = "black")
Label(root, text = "Fill out all fields", bg='red').pack()


#DEFINE FUNCTIONS#

#This one takes user input and runs appropriate roll function
def getroll():
    if dmchecktxt.get().lower() == "acrobatics":
        getrollcalc(dexteritytxt, chk_stateacrobatics)
    elif dmchecktxt.get().lower() == "animal handling":
        getrollcalc(wisdomtxt, chk_stateanimalhandling)
    elif dmchecktxt.get().lower() == "arcana":
        getrollcalc(intelligencetxt, chk_statearcana)
    elif dmchecktxt.get().lower() == "athletics":
        getrollcalc(strengthtxt, chk_stateathletics)
    elif dmchecktxt.get().lower() == "deception":
        getrollcalc(charismatxt, chk_statedeception)
    elif dmchecktxt.get().lower() == "history":
        getrollcalc(intelligencetxt, chk_statehistory)
    elif dmchecktxt.get().lower() == "insight":
        getrollcalc(wisdomtxt, chk_stateinsight)
    elif dmchecktxt.get().lower() == "intimidation":
        getrollcalc(charismatxt, chk_stateintimidation)
    elif dmchecktxt.get().lower() == "investigation":
        getrollcalc(intelligencetxt, chk_stateinvestigation)
    elif dmchecktxt.get().lower() == "medicine":
        getrollcalc(wisdomtxt, chk_statemedicine)
    elif dmchecktxt.get().lower() == "nature":
        getrollcalc(intelligencetxt, chk_statenature)
    elif dmchecktxt.get().lower() == "perception":
        getrollcalc(wisdomtxt, chk_stateperception)
    elif dmchecktxt.get().lower() == "performance":
        getrollcalc(charismatxt, chk_stateperformance)
    elif dmchecktxt.get().lower() == "persuasion":
        getrollcalc(charismatxt, chk_statepersuasion)    
    elif dmchecktxt.get().lower() == "religion":
        getrollcalc(intelligencetxt, chk_statereligion)
    elif dmchecktxt.get().lower() == "sleight of hand":
        getrollcalc(dexteritytxt, chk_statesleightofhand)
    elif dmchecktxt.get().lower() == "stealth":
        getrollcalc(dexteritytxt, chk_statestealth)
    elif dmchecktxt.get().lower() == "survival":
        getrollcalc(wisdomtxt, chk_statesurvival)
    else:
        a = Label(root, text="Error 69: I cannot check for '" + str(dmchecktxt.get()) + "'")
        a.pack(side="bottom")

#This one actually calculates what the roll command is
def getrollcalc(attributetxt, chkstateskill):
    try:    
        attribute = int(attributetxt.get())
        if attribute >= 10:
          attributemod = int((attribute - 10)/2)
        else:
            attributemod = int(((attribute - 10)/2)-.5)
        if chkstateskill.get():
            attributemod = attributemod + int(proficiencytxt.get())
        root.clipboard_clear()
        if chk_stateadvantage.get():
            root.clipboard_append("/roll 2d20 + " + str(attributemod))
            a = Label(root, text="/roll 2d20 + " + str(attributemod))
            a.pack(side="bottom")
        else:
            root.clipboard_append("/roll 1d20 + " + str(attributemod))
            a = Label(root, text="/roll 1d20 + " + str(attributemod))
            a.pack(side="bottom")
    except ValueError:
        a = Label(root, text="Error 420: Missing ability score or proficiency modifier")
        a.pack(side="bottom")

#This saves time when creating and packing check buttons and is put into upper frame
def chk_state(textname, checkname):
    chk = Checkbutton(proficiencyframe, text = textname, var=checkname) 
    chk.pack(side = "left")

#This saves time when creating and packing check buttons and is put into lower frame
def chk_statee(textname, checkname):
    chk = Checkbutton(proficiencyframe2, text = textname, var=checkname)
    chk.pack(side = "left")


#ATTRIBUTE INPUTS AND LABELS
attributeframe = Frame(root, padx=5, pady=5)
attributeframe.pack(side='top')
Label(root, text="    ").pack()
Label(attributeframe, text = "Strength").grid(row=0, column=0)
strengthtxt = Entry(attributeframe ,width=10)
strengthtxt.grid(row=1, column=0, padx=5)
Label(attributeframe, text = "Dexterity").grid(row=0, column=1)
dexteritytxt = Entry(attributeframe,width=10)
dexteritytxt.grid(row=1, column=1, padx=5)
Label(attributeframe, text = "Constitution").grid(row=0, column=2)
constitutiontxt = Entry(attributeframe,width=10)
constitutiontxt.grid(row=1, column=2, padx=5)
Label(attributeframe, text = "Intelligence").grid(row=0, column=3)
intelligencetxt = Entry(attributeframe,width=10)
intelligencetxt.grid(row=1, column=3, padx=5)
Label(attributeframe, text = "Wisdom").grid(row=0, column=4)
wisdomtxt = Entry(attributeframe,width=10)
wisdomtxt.grid(row=1, column=4, padx=5)
Label(attributeframe, text = "Charisma").grid(row=0, column=5)
charismatxt = Entry(attributeframe,width=10)
charismatxt.grid(row=1, column=5, padx=5)
Label(root, text = "Proficiency Bonus").pack()
proficiencytxt = Entry(root,width=10)
proficiencytxt.pack(side = "top")



#FORMATTING ELEMENTS: FRAMES, LABELS
Label(root, text="    ").pack()
Label(root, text="Proficiencies", bg="yellow").pack(fill="x")

proficiencyframe = Frame(root, padx=5, pady=5)
proficiencyframe.pack()
proficiencyframe2 = Frame(root, padx=5, pady=5)
proficiencyframe2.pack()
Label(root, text="    ", bg = "yellow").pack(fill="x")
advantageframe = Frame(root, padx=10, pady=10)
advantageframe.pack(fill='x')
Label(advantageframe, text="Roll with advantage").pack()
bottomframe = LabelFrame(root, text="What do you want to check?", padx=5, pady=5)
bottomframe.pack(side="bottom")
dmchecktxt = Entry(bottomframe, width=50)
dmchecktxt.pack()
Button(bottomframe, text="Calculate Roll", bg = "green", command=getroll).pack(side = "bottom", fill="x")


#DEFINITION OF CHECKBUTTONS
chk_stateacrobatics = BooleanVar()
chk_stateanimalhandling = BooleanVar()
chk_statearcana = BooleanVar()
chk_stateathletics = BooleanVar()
chk_statedeception = BooleanVar()
chk_statehistory = BooleanVar()
chk_stateinsight = BooleanVar()
chk_stateintimidation = BooleanVar()
chk_stateinvestigation = BooleanVar()
chk_statemedicine = BooleanVar()
chk_statenature = BooleanVar()
chk_stateperception = BooleanVar()
chk_stateperformance = BooleanVar()
chk_statepersuasion = BooleanVar()
chk_statereligion = BooleanVar()
chk_statesleightofhand = BooleanVar()
chk_statestealth = BooleanVar()
chk_statesurvival = BooleanVar()
chk_stateadvantage = BooleanVar()
Checkbutton(advantageframe, text='', var=chk_stateadvantage).pack()


#CHECKBUTTONS
chk_state("Acrobatics", chk_stateacrobatics)
chk_state("Animal Handling", chk_stateanimalhandling)
chk_state("Arcana", chk_statearcana)
chk_state("Athletics", chk_stateathletics)
chk_state("Deception", chk_statedeception)
chk_state("History", chk_statehistory)
chk_state("Insight", chk_stateinsight)
chk_state("Intimidation", chk_stateintimidation)
chk_state("Investigation", chk_stateinvestigation)
chk_statee("Medicine", chk_statemedicine)
chk_statee("Nature", chk_statenature)
chk_statee("Perception", chk_stateperception)
chk_statee("Performance", chk_stateperformance)
chk_statee("Persuasion", chk_statepersuasion)
chk_statee("Religion", chk_statereligion)
chk_statee("Sleight Of Hand", chk_statesleightofhand)
chk_statee("Stealth", chk_statestealth)
chk_statee("Survival", chk_statesurvival)


root.mainloop()

