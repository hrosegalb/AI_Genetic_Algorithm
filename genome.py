class Genome(object):
    def __init__(self, sequence):
        ''':param sequence: List of integers
           
           Sets self.__sequence to the sequence passed in.'''
        self.__sequence = sequence
        self.__fitness = 0


    def determine_fitness(self, vals, weights, max_weight):
        ''':param vals: List of integers
           :param weights: List of integers
           :param max_weight: integer

           Iterates through self.__sequence and determines the fitness of the Genome. If the weight of the items
           is greater than max_weight, it sets self.__fitness to 0. Otherwise, it sets self.__fitness to the total
           combined value of the selected items in the sequence.'''

        total_weight = 0
        for i in range(len(self.__sequence)):
            if self.__sequence[i] == 1:
                total_weight += weights[i]
                if total_weight > max_weight:
                    self.__fitness = 0
                    break
                else:
                    self.__fitness += vals[i]

    
    def get_sequence(self):
        return self.__sequence

    
    def get_fitness(self):
        return self.__fitness


    def print(self):
        print("Sequence: {0}\nFitness: {1}".format(self.__sequence, self.__fitness))

        
