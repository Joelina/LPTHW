from sys import exit

def first_left():
    print "You go through the first door on your left. It's a closet. There's nothing in here."
    print "You leave."
    start_new()

def second_left():
    print "You go through the second door on your left. It's the dining room."
    print "You're not alone. A maid who was decking the table looks at you."
    print "\"Yes? how can I help you?\""
    print "Do you say 1. \"I am looking for a way out.\""
    print "Or do you say 2. \"Oh, I, uh, just wanted to have some tea.\""
    pick_answer = False

    while pick_answer == False:
        choice = raw_input("> ")

        if choice == "1":
            pick_answer = True
            print "She looks at you and frowns. Finally she says: \"Talk to the old man in the seating room.\""
            start_new()
        elif choice == "2":
            pick_answer = True
            dead("""
            She nods and smiles. \"You're in luck, I just made some.\"
            She looks at the four cups in front of her, frowns and gives you one.
            You politely thank her and take a sip. Sadly the tea is poisoned and you die.
            Just so you know, the maid didn't mean to kill, she just mixed up the cups.""")
        else:
            print "Sorry, you can't just pick another option."

def first_right():
    print "You go through the first door on your right and find yourself in the library."
    print "Suddenly a ghost appears. The ghost says, \"Boo! Did I scare you?\""
    print "Do you answer 1. \"Yes, please don't hurt me!\""
    print "Or do you answer 2. \"No, you look like a nice ghost.\""
    pick_answer = False

    while pick_answer == False:
        choice = raw_input("> ")

        if choice == "1":
            pick_answer = True
            dead("The ghost lets out an evil laugh. It freaks you out so much, that you curl up in a corner and can't move anymore.")
        elif choice == "2":
            pick_answer = True
            print "The ghost smiles and says:"
            print """
            Thank you, finally someone who thinks that way. Because you were nice to me,
            I'll be nice to you. If you want to get past the guard you need to bribe him!
            There's supposed to be a treasure in a hidden room behind this bookshelf.
            You just have to take out \'The Tales of Beedlethe Bard\'.
            """
            print "You take out the book and the bookshelf reveals a hidden room."
            print "There are two levers in the room, one to the left and one to the right. Which one do you pull?"
            pick_again = False

            while pick_again == False:
                choice = raw_input("> ")

                if "left" in choice:
                    pick_again = True
                    print "A small safe that looked like the wall opens. You find 361 gold coins in it."
                    print "You take it and go back through the library into the hallway."
                    start_new()
                elif "right" in choice:
                    pick_again = True
                    dead("A trapdoor right underneath you opens up. You fall down the shaft and die.")
                else:
                    print "Sorry, you can't just pick another option."
        else:
            print "Sorry, you can't just pick another option."

def second_right():
    print "You go through the second door on your right and enter the seating room."
    print "An old man sits over a small book in an armchair. He looks up when you enter and grunts: \"What?\""
    print "Do you say 1. \"Sorry to bother you, but I am looking for a way out.\""
    print "Or do you say 2. \"Oh, nothing, wrong room. Sorry.\""
    pick_answer = False

    while pick_answer == False:
        choice = raw_input("> ")

        if choice == "1":
            pick_answer = True
            print "\"Sure. But only if you solve my riddle:\""
            print "\"The more you take, the more you leave behind. What is it?\""
            pick_again = False

            while pick_again == False:
                choice = raw_input("> ")

                if "Footsteps" in choice or "footsteps" in choice:
                    pick_again = True
                    print "\"Well done! You will need a code for the door behind the guard. The code is the answer to this riddle:\""
                    print "\"What number comes next? 2, 2, 4, 12, 48, _.\""
                    pick_again_again = False

                    while pick_again_again == False:
                        choice = raw_input("> ")

                        if choice == "240":
                            pick_again_again = True
                            print "\"Well done! You are a true riddler! Good luck on your way out!\""
                            print "You thank the old man and go back into the hallway."
                            start_new()
                        else:
                            print "Wrong, try again!"
                else:
                    print "Wrong, try again!"

        elif choice == "2":
            pick_answer = True
            dead("""You want to leave, but the old man yells: \"STOP RIGHT THERE!\"
            Terrified you turn around. He grins. \"You haven't solved my riddle yet.\"
            His riddle is so ridiculous and unsolvable that you turn mad and are unable to do anything anymore.""")
        else:
            print "Sorry, you can't just pick another option."

def guard_talk():
    print "You go talk to the guard. After you mention your request to leave he says:"
    print "\"Sorry, I'm ordered to not let anybody out. It's my job. But I could be persuaded.\""
    print "How many gold coins will you give me?"

    choice = raw_input("> ")

    if choice == "361":
        print "You show the guard the gold coins you found. He takes them and lets you pass."
        print "You have to type in a code to open the door."

        choice = raw_input("> ")

        if choice == "240":
            print "Congratulations, you are free! Thank you for playing!"
            exit(0)
        else:
            print "That's the wrong code. You have to go back and find the code."
            start_new()

    else:
        print "You don't have anything to give the guard. He won't let you through until you find something."
        start_new()

def dead(why):
    print why, "Thanks for playing!"
    exit(0)

def start_new():
    print "You are back in the hallway. What do you do next?"

    choice = raw_input("> ")

    if "1" in choice or "first" and "left" in choice:
        first_left()
    elif "2" in choice or "second" and "left" in choice:
        second_left()
    elif "3" in choice or "first" and "right" in choice:
        first_right()
    elif "4" in choice or "second" and "right" in choice:
        second_right()
    elif "5" in choice or "talk" and "guard" in choice:
        guard_talk()
    else:
        dead("You don't want to leave? Well, no adventure for you then.")

def start():
    print "You find yourself in the hallway of a rather old mansion."
    print "You can't seem to remember how you got here, but you do know that it's time to leave."
    print "There are 4 doors, 2 to the left and 2 to the right."
    print "There is a fifth door at the far end of the corridor, which is guarded by a grim looking man in uniform."
    print "What do you do?"
    print "1. Go through the first door on your left."
    print "2. Go through the second door on your left."
    print "3. Go through the first door on your right."
    print "4. Go through the second door on your right."
    print "5. Talk to the guard."

    choice = raw_input("> ")

    if "1" in choice or "first" and "left" in choice:
        first_left()
    elif "2" in choice or "second" and "left" in choice:
        second_left()
    elif "3" in choice or "first" and "right" in choice:
        first_right()
    elif "4" in choice or "second" and "right" in choice:
        second_right()
    elif "5" in choice or "talk" and "guard" in choice:
        guard_talk()
    else:
        dead("You don't want to leave? Well, no adventure for you then.")

start()
