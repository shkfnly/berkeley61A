# A "simple" adventure game.

# README:
# http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab09/lab09.txt

name = 'Player 1' # Can replace this with your name. :)
me = None # Will be initalized to Person(name) after Person class is defined

def adventure():
    while True:
        check_win_conditions(me, Place)
        try: # In case of errors... catch them!
            Place.current.describe()
            line = input('adventure> ')
            exp = adv_parse(line)
            output = adv_eval(exp)
            print(output)
            print('\n') # New line for neatness
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except (SyntaxError, NameError, KeyError, TypeError, IndexError) as e:
            print('ERROR:', e)


def adv_parse(line):
    """ Parses adventure.py commands

    Handles things differently when
    the first part of the string is 'give'
    or 'ask'

    >>> adv_parse('look')
    ('look', '')
    >>> adv_parse('take rubber ducky')
    ('take', 'rubber ducky')
    >>> adv_parse('give rubber ducky to Andrew')
    ('give', 'rubber ducky', 'Andrew')
    >>> adv_parse('ask Andrew for advice about the midterm')
    ('ask', 'Andrew', 'advice about the midterm')
    """
    tokens = line.split()
    if not tokens: # empty list
        raise SyntaxError('No command given')
    token = tokens.pop(0)
    if token == 'give':
        target = tokens.pop(-1)
        delete_to = tokens.pop(-1)
        return (token, ' '.join(tokens[0:]), target)
    elif token == 'ask':
        target = tokens.pop(0)
        delete_for = tokens.pop(0)
        return (token, target, ' '. join(tokens[0:]))
    else: # Only split out the operator, the rest must be the operand
        return (token, ' '.join(tokens[0:]))


def adv_eval(exp):
    if is_operator(exp): # Use the underlying eval to grab the
        return eval(exp) # function that implements the action.
    if is_person(exp):
        return Person.people[exp]
    elif isinstance(exp, str): # If we're describing something,
        return exp             # just output it.
    elif exp[0] == 'give':
        return give(adv_eval(exp[2]), exp[1])
    elif exp[0] == 'ask':
        return ask(adv_eval(exp[1]), exp[2])
    elif exp[0] == 'stuff':
        for item in me.inventory:
            print(item.name + " - " + item.examine())
    else:
        return adv_apply(exp[0], exp[1])


def adv_apply(operator, operand):
    if operator == 'look':
            return look(operand)
    elif operator == 'go':
            return go(operand)
    elif operator == 'take':
            return take(operand)
    elif operator == "examine":
        return examine(operand)
    elif operator == "help":
        return help(operand)
    else:
        return TypeError(operator + ' is an unknown operator')

def is_person(exp):
    return exp in Person.people

def check_win_conditions():
    pass

# We shouldn't define the following functions in the global frame.  There are
# better ways of doing this (generic operator FTW), but for simplicity's sake,
# this is what I'm going with.

def is_operator(exp):
    return exp in ('look', 'go', 'take', 'give', 'ask',
                   'examine', 'help')

def look(_):
    return Place.current.look()

def go(direction):
    output = Place.current.exit_to(direction)
    return output

def take(thing):
    obj = Place.current.find(thing)
    if obj:
        return me.take(obj)
    return 'No such thing to take!'

def give(person, thing):
    if type(person) != Person:
        return "Who is {}?!".format(person)
    if person not in Place.current.people:
        return person.name + ' not here!'
    obj = None
    for i, e in enumerate(me.inventory):
        if thing in e.name:
            obj = me.inventory.pop(i)
    if obj:
        return person.take(obj)
    return "You don't have this in your possession!"

def ask(person, message):
    if type(person) != Person:
        return "Who is {}?!".format(person)
    return person.ask(message)

def examine(thing):
    for item in me.inventory:
        if thing in item.name:
            return item.examine()
    return "You don't have this in your possession!"

def help(_):
    return \
"""There are 7 possible operators:
  * look
  * go [direction]
  * take [thing]
  * give [thing] to [person]
  * examine [thing in inventory]
  * ask [person] for [message]
  * help"""


# OOP representation of the game models:
class Person(object):
    people = {}
    def __init__(self, name, *things):
        self.name = name
        self.inventory = list(things)
        Person.people[name] = self

    def think(self, msg):
        return self.name + 'remains silent'

    def take(self, thing):
        self.inventory.append(thing)
        return self.name + ' takes the ' + thing.name

    def ask(self, msg):
        return self.think(self, msg) # Because we override think with a function


# Need to initalize after Person class exists
me = Person(name)


class Place(object):
    current = None
    def __init__(self, name, description, *people_and_things):
        self.name = name
        self.description = description
        self.people = []
        self.things = []
        self.exits = {}
        for obj in people_and_things:
            if type(obj) == Person:
                self.people.append(obj)
            elif type(obj) == Thing:
                self.things.append(obj)

    def describe(self):
        print(self.description)
        if self.exits:
            print('\nExits:')
            for k, v in self.exits.items():
                print('  ', k, '-', v[0].name)
        print()

    def look(self):
        result = 'You take a look around and see:\n'
        if not (self.people or self.things):
            result += 'Nothing!'
        result += '\n'.join([thing.name + ' - ' + thing.description for thing in self.things])
        result += '\n'.join([person.name for person in self.people])
        return result

    def exit_to(self, exit):
        if exit in self.exits:
            new_place, exit_msg = self.exits[exit]
            Place.current = new_place
            return exit_msg
        return "Where do you think you're going?!"

    def find(self, thing):
        for i, e in enumerate(self.things):
            if thing in e.name:
                return self.things.pop(i)
            

class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def examine(self):
        return self.description
  

# This is what @main does (sorta)
if __name__ == '__main__':
    try:
        from cs61a_world import *

        me = Person(name)
        print(motd)
        adventure()
    except ImportError as e:
        print("ERROR: Something terrible happened to cs61a_world.py")
        print("\t Invalid or broken world.")
        print(e)
    except IndexError as e:
        print("ERROR: Could not load world. Did you forget to provide it?")
        print("\tExample: python3 adventure.py cs61as_world")
        print(e)