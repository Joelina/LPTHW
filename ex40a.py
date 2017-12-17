mystuff = {'apple': "I AM APPles!"}
print mystuff['apple']

import mystuff
mystuff.apple

def apple():
    print "I AM APPLES!"

tangerine = "Living reflection of a dream"

import mystuff
mystuff.apple()
print mystuff.tangerine

mystuff['apple'] #get apple from dict
mystuff.apple #get apple from the module
mystuff.tangerine #same thing, it's just a variable

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine
