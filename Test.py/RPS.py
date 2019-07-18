import random
x=random.randint(1,3)
y=input("Pick a #. 1,2,or3. Two rounds. Rock is 1. Paper is 2. Scissors is 3.")
if x == 1:
    choice="Rock"
if x == 2:
    choice="Paper"
if x == 3:
    choice="Scissors"
    
if("y==2") and (choice=="Rock"):
    y=input("Won. Round 2")
    if("y==1") and (choice=="Rock"):
        y=input("Tie. Round 2")
    elif("y==3") and (choice=="Rock"):
        y=input("Lost. Round 2")
    elif("y==1") and (choice=="Paper"):
        y=input("Lost. Round 2 ")
    elif("y==2") and (choice=="Paper"):
        y=input("Tie. Round 2")
    elif("y==3") and (choice=="Paper"):
        y=input("Won. Round 2")
    elif("y==1") and (choice=="Scissors"):
        y=input("Won. Round 2")
    elif("y==2") and (choice=="Scissors"):
        y=input("Lost. Round 2")
    elif("y==3") and (choice=="Scissors"):
        y=input("Tie. Round 2")

elif("y==1") and (choice=="Rock"):
    y=input("Tie. Round 2")
    if("y==2") and (choice=="Rock"):
        y=input("Won. Round 2")
    elif("y==3") and (choice=="Rock"):
        y=input("Lost. Round 2")
    elif("y==1") and (choice=="Paper"):
        y=input("Lost. Round 2 ")
    elif("y==2") and (choice=="Paper"):
        y=input("Tie. Round 2")
    elif("y==3") and (choice=="Paper"):
        y=input("Won. Round 2")
    elif("y==1") and (choice=="Scissors"):
        y=input("Won. Round 2")
    elif("y==2") and (choice=="Scissors"):
        y=input("Lost. Round 2")
    elif("y==3") and (choice=="Scissors"):
        y=input("Tie. Round 2")
elif("y==3") and (choice=="Rock"):
    y=input("Lost. Round 2")
    if("y==1") and (choice=="Rock"):
        y=input("Tie. Round 2")
    elif("y==2") and (choice=="Rock"):
        y=input("Won. Round 2")
    elif("y==1") and (choice=="Paper"):
        y=input("Lost. Round 2 ")
    elif("y==2") and (choice=="Paper"):
        y=input("Tie. Round 2")
    elif("y==3") and (choice=="Paper"):
        y=input("Won. Round 2")
    elif("y==1") and (choice=="Scissors"):
        y=input("Won. Round 2")
    elif("y==2") and (choice=="Scissors"):
        y=input("Lost. Round 2")
    elif("y==3") and (choice=="Scissors"):
        y=input("Tie. Round 2")
elif("y==1") and (choice=="Paper"):
    y=input("Lost. Round 2 ")
    elif("y==3") and (choice=="Rock"):
        y=input("Lost. Round 2")
    if("y==1") and (choice=="Rock"):
        y=input("Tie. Round 2")
    elif("y==2") and (choice=="Rock"):
        y=input("Won. Round 2")
    elif("y==2") and (choice=="Paper"):
        y=input("Tie. Round 2")
    elif("y==3") and (choice=="Paper"):
        y=input("Won. Round 2")
    elif("y==1") and (choice=="Scissors"):
        y=input("Won. Round 2")
    elif("y==2") and (choice=="Scissors"):
        y=input("Lost. Round 2")
    elif("y==3") and (choice=="Scissors"):
        y=input("Tie. Round 2")
elif("y==2") and (choice=="Paper"):
    y=input("Tie. Round 2")
elif("y==3") and (choice=="Paper"):
    y=input("Won. Round 2")
elif("y==1") and (choice=="Scissors"):
    y=input("Won. Round 2")
elif("y==2") and (choice=="Scissors"):
    y=input("Lost. Round 2")
elif("y==3") and (choice=="Scissors"):
    y=input("Tie. Round 2")
