"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

class Person:
    def __init__(self, firstname, lastname, gender):
        if ((gender=='M') or (gender=='F')):
           self.gender = gender
        else:
           print "Gender must be M or F"
        self.firstname = firstname[0].upper() + firstname[1:]
        self.lastname = lastname[0].upper() + lastname[1:]
    def sayname(self):
        print "{} {}".format(self.firstname, self.lastname)
    def saygender(self):
        print self.gender

class Building:
    tracker = {}
    __all__ = set()

    def __init__(self,location):
       Building.__all__.add(self)
       self.location=location

    def enter(self, person, room_no):
        self.tracker[person] = room_no

    def __setitem__(self, room_no, person):
        self.tracker[person] = room_no

    def where_is(self, person):
        if person in self.tracker:
            print "{} is in room {}".format(person.firstname, self.tracker[person])
        else:
            print "{} is not in the building".format(person.firstname)

    def rollcall(self):
        for person in self.tracker:
            print "{} is in the building!".format(person.firstname)

class OfficeBuilding(Building,object):
    def __init__(self, employees,location):
       self.employees = employees
       super(OfficeBuilding,self).__init__(location)
    
    def enter(self, person, room_no):
       if any(employee == person for employee in self.employees):
           super(OfficeBuilding,self).enter(person,room_no)
       else:
           print "Access denied"

class House(Building,object):

    def __init__(self,location):
        super(House,self).__init__(location)

    def enter(self, person):
        self.inside=person
    def at_home(self, person):
        if self.inside==person:
            print "At home!"
        else:
            print "Not home"
    def where_is(self, person):
        raise Exception("Not defined for a house")

def buildinglocations(location):
    found=False
    print "at {}:".format(location)
    for building in Building.__all__:
        if building.location==location:
            print building.__class__.__name__
            found=True
    if found==False:
        print "No building here"
