class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, arg):
        my_score = (self.goals * 3) + self.points
        arg_score = (arg.goals * 3) + arg.points
        if my_score > arg_score:
            return True
        else:
            return False

    def less_than(self, arg):
        my_score = (self.goals * 3) + self.points
        arg_score = (arg.goals * 3) + arg.points
        if my_score < arg_score:
            return True
        else:
            return False

    def equal_to(self, arg):
        my_score = (self.goals * 3) + self.points
        arg_score = (arg.goals * 3) + arg.points
        if my_score == arg_score:
            return True
        else:
            return False
