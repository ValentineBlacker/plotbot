''' Random Plot Generator Extension
    Valentine Blacker
    Oct 2011
'''
import random
import sys


class Plotter(object):
    def __init__(self):
        pass

    def choose_random_item(self, item_type):
        line = random.choice(open('{0}.txt'.format(item_type)).readlines())
        line = line.rstrip('\n')
        if item_type[-3:] == 'adj':
            line = self.articleizer(line)
        return line

    def articleizer(self, input_line):
        return_line = ("an " + input_line if input_line[0] in 'aeiou' else "a "+input_line)
        return return_line

    def make_plot(self):
        adjective = self.choose_random_item('heroadj')
        hero=  self.choose_random_item('hero')
        hero_string = adjective +" "+hero+" "
        split = random.randrange(2)
        if split == 0:
            enemy =  self.choose_random_item('enemy')
            middle_string = "fights "+enemy+" "
        elif split == 1:
            objectstypes = self.choose_random_item('objectstypes')
            objects = self.choose_random_item('objects')
            middle_string = "quests for "+objectstypes+ " "+objects+" "
        split = random.randrange(2)
        if split == 0:
            bossadj =   self.choose_random_item('bossadj')
            boss = self.choose_random_item('boss')
            end_string =  "to defeat "+bossadj + " " + boss + ""
        elif split == 1:
            saved = self.choose_random_item("save")
            end_string = "to save their " + saved
        location = self.choose_random_item('location')+ " "

        print("Your random plot is: ")
        plotstring = (hero_string+ middle_string+location +end_string+"!").capitalize()
        print(plotstring)
        print len(plotstring)

if __name__ == '__main__':
    plotter = Plotter()
    plotter.make_plot()
    sys.exit(0)
