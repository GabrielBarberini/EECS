from random_walk import Drunk
from random_walk import Usual_drunk
from random_walk import drunk_test 
import random

class Cold_drunk(Drunk):
    def take_step(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0,0.0), (-1.0,0.0)] 
        return random.choice(stepChoices)

class EW_drunk(Drunk):
    def take_step(self):
        stepChoices = [(1.0,0.0), (-1.0,0.0)] 
        return random.choice(stepChoices)

def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)

sim_all((Usual_drunk, Cold_drunk, EW_drunk), (100, 1000),10)


