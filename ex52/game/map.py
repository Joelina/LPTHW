class Scene(object):

    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

    def get_paths(self):
        return self.paths

central_corridor = Scene("Central Corridor", "central_corridor",
"""
An evil sorcerer has kidnapped your best friend and locked them up in a tower.
You have to fight your way through his castle to the tower to save your best
friend and flee with them.

You just entered the castle and find yourself in the central corridor.
As you run towards the door at the other end of the corridor, a dark
gruesome looking demon with yellow eyes appears in front of you.
You skid to a halt as he is about to blast a spell at you.
""")

big_hall_01 = Scene("Big Hall", "big_hall_01",
"""
With your super quick reflexes you dodge his spell doing awesome rolls,
jumps and somersaults. Sadly you're a bit clumsy. While doing a graceful
pirouette you slip and fall on your cute bottom. You look up with such a
puzzled look on your face that the demon starts roaring with laughter and
evaporates. Good thing your clumsiness is hilarious.

You stumble through the door into a big hall. As soon as your in you realize
that 5 more demons are looking directly at you. They have gleaming red eyes
and look even worse than the one before. You see that the biggest demon
has a key around his neck. the door to the tower is on the other side of the hall.
""")

big_hall_02 = Scene("Big Hall", "big_hall_02",
"""
You recognize the demon from a book you've recently read. You remember it saying
that this demon can be defeated if you make it laugh. You tell the only joke you
can remember: \"What do you call a group of unorganized cats? A cat-astrophy!\"
The demon stops and just looks at you. You hold your breath.
Suddenly the demon bursts into laughter and evaporates. You're glad you remembered
that joke and hurry through the door.

You stumble through the door into a big hall. As soon as your in you realize
that 5 more demons are looking directly at you. They have gleaming red eyes
and look even worse than the one before. You see that the biggest demon
has a key around his neck. the door to the tower is on the other side of the hall.
""")

the_tower = Scene("The Tower", "the_tower",
"""
You remember from your book, that red eyed demons can't really see
but rather find their targets through sound waves. That also explains
why they haven't done anything yet. As quietly as you can you make your
way past the first 4 demons. They all still stare at the door you came
through. You manage to sneak up on the biggest demon and try to snatch
the key. It's harder than you thought but finally you got it! You continue
to sneak your way to the other door and make it through.

You find yourself at the bottom of some stairs. They must lead up to
the tower! You run up all the way until you stand in front of another door.
The key you stole from the demon seems to fit the lock, but as you approach
the door the lock transforms into a face. It looks at you and says:

\"Solve this riddle, but not in a haste.
Answer it wrong and you'll go to waste.
Answer it right and you'll be rewarded
As this very door will no longer be guarded.
The riddle is as follows, so open your ears:
What comes once in a minute, twice in a moment, but never in a thousand years?\"
""")

next_question = Scene("Next Question", "next_question",
"""

The face smiles and says:
\"Very well done, now go on ahead
Or stay were you are until you are dead.\"
The face transforms back into the lock. You put the key in and turn it.

The door opens. You can see your best friend lying on the floor,
apparently unconscious. There are three bottles and a piece of paper on
the desk next to them. The paper reads:
To save your friend you simply must choose
The bottle that wakes him, which won't be the booze.
Please beware of the poison as well
Or you'll send your friend straight into hell.
""")

dragons_den = Scene("Dragons Den", "dragons_den",
"""
You take bottle 2 and open it. You try to smell what it is but are left
absolutey clueless. Before pouring it into your best friends' mouth you
try it yourself. You take a sip but nothing happens. Carefully you give
a little to your best friend. Their eyes open. You did it!
They say: \"Where are we, what's going on?\"
You just say that there's no time to explain and that you'll have to get
the hell out of there. You help them up and together you leave the tower.

You run down the stairs of the tower and back into the big hall.
You nearly forgot about the demons and quickly rush through the next best door.
You find yourselves in a very odd looking room. It seems to be more of a cave,
but at the same time also looks like a stable of some sort. You sneak further
into the room and look around a corner just to see an enormous silvery blue dragon
standing right in front of you.
""")

the_end_winner = Scene("You made it!", "the_end_winner",
"""
You remember that you have some fruit in your pocket. You take it out and hold it
in front of the dragon. The dragon starts wagging its tail. You say: \"Who's a good dragon?\"
and the dragons' tail wags even more. You say: \"Sit!\" and the dragon sits. You carefully
place the fruit in front of the dragon and say: \"Wait!\" The dragon howls a little.
You say: \"And go.\" The dragon happily eats the fruit. You go pet the dragon and see that
there's a big double door behind it. You open it and find that it leads to the top of a cliff.
Your best friend says: \"Let's take the dragon to get out!\" You look at them like their crazy
just to realize that there's no other option. You two climb onto the dragon and flee from this evil place.
""")

the_end_loser = Scene("So close", "the_end_loser",
"""
Sadly you are not quick enough. The dragon lets out an angry howl
and then torches the two of you with a fireball.
""")

generic_death = Scene("Game over", "death",
"""
Trying to fight a demon is like trying to touch fire - you get burned.
""")

coward_death = Scene("Game over", "death",
"""
You seriously just want to up and run? How can you betray your best friend like that?
You are such a coward! As you run back the way you came, you trip and fall into the
dark abyss of guilt. That's what you get!
""")

smart_death = Scene("Game over", "death",
"""
As they look similar to the demon you just met you try defeating them
with your joke. After you told the joke, the demons look even angrier than
before and all come at you at once. You close your eyes and remember that
red eyed demons get angry at jokes and that they're not to be mistaken with
the yellow eyed demons. Sadly you remembered that too late.
""")

poison_death = Scene("Game over", "death",
"""
You take a bottle at random, open it and try to smell what its content could be.
You don't seem to smell anything. Before pouring it into your best friends' mouth
you decide to try it yourself. You take a sip and immediately collapse onto the floor.
You chose the poison.
""")

wrong_answer_death = Scene("Game over", "death",
"""
The face says:
\"Your answer was wrong, so this is goodbye.
Just close your eyes and prepare to die.\"
A trap door opens uo underneath you. You fall down all the way thorugh the tower
and die the moment you hit the ground.
""")

dragons_den.add_paths({
    'fight': the_end_loser,
    'give food': the_end_winner,
    'flee': the_end_loser
})

the_tower.add_paths({
    '*': wrong_answer_death,
    'The letter m': next_question
})

next_question.add_paths({
    '1': poison_death,
    '2': dragons_den,
    '3': poison_death
})

big_hall_01.add_paths({
    'fight!': generic_death,
    'tell a joke!': smart_death,
    'use stealth!': the_tower
})

big_hall_02.add_paths({
    'fight!': generic_death,
    'tell a joke!': smart_death,
    'use stealth!': the_tower
})

central_corridor.add_paths({
    'fight!': generic_death,
    'flee!': coward_death,
    'dodge!': big_hall_01,
    'tell a joke!': big_hall_02
})

SCENES = {
    central_corridor.urlname : central_corridor,
    big_hall_01.urlname : big_hall_01,
    big_hall_02.urlname : big_hall_02,
    the_tower.urlname : the_tower,
    next_question.urlname : next_question,
    dragons_den.urlname : dragons_den,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death
}
START = central_corridor
