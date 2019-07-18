import random
z=random.randint(1,3)
run="1"
fight="2"
right="3"
left="4"
fowards="5"
around="6"
through="7"
desert="8"
horde="9"
run2="10"
left2="11"
right="12"
print("A zomibe is coming towards you.You can run or fight.You have a  katana")
y=input("Do you want to run or fight.Run is 1.Fight is 2.")
if y=="2":
    if z==1:
        print("You slice off the zombie's head and find your friends. Victory")
    elif z==2:
        print("You stab the zombie, killing him, but breaking your katana. You have to run from thee battle. From a bush, you see your friends run into and die from the zombie. You then run. Defeat")
    elif z==3:
        print("You miss your first swipe, letting the zombie get to close and kill you.RIP")
        
if y=="1":
    print("You escaped the zombie horde, but you need to find your friends.")
    x=input("You come at a crossroad. Do you go left,stright, or right?\nRight is 3, Fowards is 5 and Left is 4")
    if x=="3":
        b=input("You turn right and go into a desert. You have a canteen of water to brace it. You can hear the horde behind you. Do you run in the desert or face the horde? Desert is 8 and horde is 9")
        if (b=="8") or (b=="9"):
            print("You died")
    elif x=="4":
        b=input("You turn left and see a massive path. It is riddled with zombies. You also see that it branches several times. As you walk the path, killing zombies, you get lost. You don't mind that to much untill you hear the zombie horde. Do you run, maybe geting more lost, or do you face the horde? The horde is 9 and running is 10.")
        if b=="9":
            print("You Died")
        if b=="10":
            c=input("You run in the oposite direction and see an exit. You empty out to another crossroad. You can go left or right.Left is 11 and Right is 12")
            if c=="11":
                print("You go left and relize it was a path back to the three crossroads. When you get there, you see people in the distant. When they get closer, you relize that they are your friends.\nVictory")
            if c=="12":
                print("You go right and quickly run into another horde, traping and killing you. Game Over")
    elif x=="5":
        a=input("You go straight. There is a massive lake, an ax, and a tree.There is also a trail that looks like it winds around the lake. You could either go around or go through. Around is 6 and through is 7.")
        if a=="6":
            print("You go on the path, and find out that it is a big loop. You then take the raft across the lake you see a path, and when you apporoch it, you find a zombie hoard that traps you in the water. You eventually die of starvation.Try again")
        if a=="7":
            b=input("You go across the lake. When you get to shore, you can see a zombie hoard on the horizon. The path away from the hoard leads to a desert. You have half a canteen of water. You can go in the desert or face the horde. Desert=8 and horde=9")
            if (b=="8") or (b=="9"):
                print("You Died")