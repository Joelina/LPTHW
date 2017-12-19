from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "Not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died and you suck. That's too bad.",
        "What will your best friend think of you?",
        "I hope you feel guilty and try again.",
        "Don't let your best friend down like this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "\nAn evil sorcerer has kidnapped your best friend"
        print "and locked them up in a tower."
        print "You have to fight your way through his castle to the tower"
        print "to save your best friend and flee with them."
        print "\n"
        print "You just entered the castle and find yourself in the"
        print "central corridor. As you run towards the door at the other end"
        print "of the corridor, a dark gruesome looking demon with yellow eyes appears"
        print "in front of you. You skid to a halt as he is about to blast a spell at you."
        print "What do you do?"
        print "1. fight"
        print "2. dodge"
        print "3. tell a joke"
        print "4. flee"

        action = raw_input("> ")

        if action == "dodge" or action == "2":
            print "\nWith your super quick reflexes you dodge his spell doing awesome"
            print "rolls, jumps and somersaults. Sadly you're a bit clumsy."
            print "While doing a graceful pirouette you slip and fall on your cute bottom."
            print "You look up with such a puzzled look on your face that the demon"
            print "starts roaring with laughter and evaporates."
            print "Good thing your clumsiness is hilarious."
            print "You check if any other demon's around and then hurry through the door."
            return 'big_hall'

        elif action == "fight" or action == "1":
            print "\nYou take out your super awesome magical sword and get ready to fight."
            print "The demon attacks you with a blasting spell and you quickly deflect it"
            print "with your sword. Then you attack. Fiercefully you run towards the demon,"
            print "jump and ram your sword into the demon."
            print "However, that didn't quite work as planned. You realize your sword is useless"
            print "against this demon as he grabs your neck and absorbs your soul."
            return 'death'

        elif action == "flee" or action == "4":
            print "\nReally, you want to flee?"
            print "You want to just leave your best friend to die?"
            print "Coward!"
            print "As you run back the way you came, you trip and fall down the dark abyss of guilt."
            print "That's what you get."
            return 'death'

        elif action == "tell a joke" or action == "3":
            print "\nYou recognize the demon from a book you've recently read."
            print "You remember it saying that this demon can be defeated if you make it laugh."
            print "You tell the only joke you can remember:"
            print "What do you call a group of unorganized cats? A cat-astrophy!"
            print "The demon stops and just looks at you. You hold your breath."
            print "Suddenly the demon bursts into laughter and evaporates."
            print "You're glad you remembered that joke and hurry through the door."
            return 'big_hall'

        else:
            print "\nSorry, you can't do that."
            return 'central_corridor'

class BigHall(Scene):

    def enter(self):
        print "\nYou stumble through the door into a big hall. As soon as your in you realize"
        print "that 5 more demons are looking directly at you. They have gleaming red eyes"
        print "and look even worse than the one before. You see that the biggest demon"
        print "has a key around his neck. the door to the tower is on the other side of the hall."
        print "What do you do?"
        print "1. fight"
        print "2. tell a joke"
        print "3. use stealth"

        action = raw_input("> ")

        if action == "tell a joke" or action == "2":
            print "\nAs they look similar to the demon you just met you try defeating them"
            print "with your joke. After you told the joke, the demons look even angrier than"
            print "before and all come at you at once."
            print "You close your eyes and remember that red eyed demons get angry at jokes and"
            print "that they're not to be mistaken with the yellow eyed demons."
            print "Sadly you remembered that too late."
            return 'death'

        elif action == "fight" or action == "1":
            print "\nYou get ready to fight and draw your magical sword."
            print "You attack the nearest demon and a marvellous fight commences."
            print "You manage to kill two demons before you start to get tired."
            print "These demons are very durable and your stamina rapidly decreases."
            print "But the thought of your best friend gives you determination and"
            print "will power. You kill another two. Only the demon carrying the key is left."
            print "You have hardly any energy left when the demon hits you."
            print "As you draw your last breath, you can't help but shed a tear."
            print "You were so close."
            return 'death'

        elif action == "use stealth" or action == "3":
            print "\nYou remember from your book, that red eyed demons can't really see"
            print "but rather find their targets through sound waves."
            print "That also explains why they haven't done anything yet."
            print "As quietly as you can you make your way past the first 4 demons."
            print "They all still stare at the door you came through."
            print "You manage to sneak up on the biggest demon and try to snatch the key."
            print "It's harder than you thought but finally you got it!"
            print "You continue to sneak your way to the other door and make it through."
            return 'the_tower'

        else:
            print "\nSorry, you can't do that."
            return 'big_hall'

class TheTower(Scene):

    def enter(self):
        print "\nYou find yourself at the bottom of some stairs. They must lead up to"
        print "the tower! You run up all the way until you stand in front of another door."
        print "The key you stole from the demon seems to fit the lock, but as you approach"
        print "the door the lock transforms into a face. It looks at you and says:"
        print """
        Solve this riddle, but not in a haste.
        Answer it wrong and you'll go to waste.
        Answer it right and you'll be rewarded
        As this very door will no longer be guarded.
        The riddle is as follows, so open your ears:
        What comes once in a minute, twice in a moment, but never in a thousand years?
        """

        answer = raw_input("> ")

        if answer == "the letter m" or answer == "the letter M":
            print "\nThe face smiles and says:"
            print """
            Very well done, now go on ahead
            Or stay were you are until you are dead.
            """
            print "The face transforms back into the lock. You put the key in and turn it."
            print "The door opens. You can see your best friend lying on the floor, apparently unconscious."
            print "There are three bottles and a piece of paper on desk next to them."
            print "The paper reads:"
            print """
            To save your friend you simply must choose
            The bottle that wakes him, which won't be the booze.
            Please beware of the poison as well
            Or you'll send your friend straight into hell.
            """
            print "Which bottle do you choose? 1, 2 or 3?"

            correct_bottle = randint(1,3)
            guess = raw_input("[bottle #]> ")

            if int(guess) != correct_bottle:
                print "\nYou take bottle %s and open it." % guess
                print "You try to smell what it is but are left absolutey clueless."
                print "Before pouring it into your best friends' mouth you try it yourself."
                print "You take a sip and immediately collapse onto the floor. You chose the poison."
                return 'death'
            else:
                print "\nYou take bottle %s and open it." % guess
                print "You try to smell what it is but are left absolutey clueless."
                print "Before pouring it into your best friends' mouth you try it yourself."
                print "You take a sip but nothing happens. Carefully you give a little to your best friend."
                print "Their eyes open. You did it!"
                print "They say: \"Where are we, what's going on?\""
                print "You just say that there's no time to explain and that you'll have to leave immediately."
                print "You help them up and together you leave."
                return 'dragons_den'

        else:
            print "\nThe face says:"
            print """
            Your answer was wrong, so this is goodbye.
            Just close your eyes and be prepared to die.
            """
            print "A trap door opens uo underneath you. You fall down all the wy thorugh the"
            print "tower and die the moment you hit the ground."
            return 'death'


class DragonsDen(Scene):

    def enter(self):
        print "\nYou run down the stairs of the tower and back into the big hall."
        print "You nearly forgot about the demons and quickly rush through the next best door."
        print "You find yourselves in a very odd looking room. It seems to be more of a cave, but"
        print "at the same time also looks like a stable of some sort."
        print "You sneak further into the room and look around a corner just to see"
        print "an enormous silvery blue dragon standing right in front of you."
        print "He looks directly at the two of you."
        print "What do you do?"
        print "1. fight"
        print "2. flee"
        print "3. give food"

        action = raw_input("> ")

        if action == "give food" or action == "3":
            print "\nYou remember that you have some fruit in your pocket. You take it"
            print "out and hold it in front of the dragon."
            print "The dragon starts wagging its tail."
            print "You say: \"Who's a good dragon?\" and the dragons' tail wags even more."
            print "You say: \"Sit!\" and the dragon sits. You carefully place the fruit in front of"
            print "the dragon and say: \"Wait!\" The dragon howls a little. You say: \"And go.\""
            print "The dragon happily eats the fruit. You go pet the dragon and see that there's a big"
            print "double door behind it. You open it and find that it leads to the top of a cliff."
            print "Your best friend says: \"Let's take the dragon to get out!\""
            print "You look at them like their crazy just to realize that there's no other option."
            print "You two climb onto the dragon and flee from this evil place."
            return 'finished'

        else:
            print "\nYou %r. That was a bad choice." % action
            print "The dragon lets out an angry howl and then torches the two of you"
            print "with a fireball."
            return 'death'

class Finished(Scene):

    def enter(self):
        print "\nYou did it! Well done!"
        print "Your best friend is proud of you!"
        print "Thank you for playing!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'big_hall': BigHall(),
        'the_tower': TheTower(),
        'dragons_den': DragonsDen(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
