class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

std = Student('H2P', 100)
std.print_score()