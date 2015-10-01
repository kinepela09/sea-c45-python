class Turtle(object):

    def __init__(self, name, color, weapon):
        self.name = name
        self.color = color
        self.weapon = weapon

    def __str__(self):
        return self.name + " wears " + self.color + \
            " and fights with a " + self.weapon

t1 = Turtle("Donatello", "purple", "bo staff")
t2 = Turtle("Raphael", "red", "sai")
t3 = Turtle("Leonardo", "orange", "pizza")
