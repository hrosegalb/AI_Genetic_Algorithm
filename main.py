import random

def determine_fitness(vals, weights, max_weight, sequence):
    ''':param vals: List of integers
       :param weights: List of integers
       :param max_weight: integer
       :param sequence: List of integers

       Iterates through sequence and determines the fitness of the genome. If the weight of the items
       is greater than max_weight, it sets fitness to 0. Otherwise, it sets fitness to the total
       combined value of the selected items in the sequence.'''

    total_weight = 0
    fitness = 0
    for i in range(len(sequence)):
        if sequence[i] == 1:
            total_weight += weights[i]
            if total_weight > max_weight:
                    fitness = 0
                    break
            else:
                fitness += vals[i]
    return fitness


def sum_fitnesses(object_list):
    ''':param object_list: List of genome lists
       
       Sums the fitnesses of each genome in the list and returns the value.'''
    return sum([object_list[i][0] for i in range(len(object_list))])


def create_genome_population(vals, weights, max_weight, num_pop):
    ''':param vals: List of integers
       :param weights: List of integers
       :param max_weight: integer
       :param num_pop: integer
       
       Creates and returns a list of genomes. Genomes consist of a list where:
       genome[0] = integer representing the fitness value of the genome
       genome[1] = list of integers representing the items chosen for knapsack'''

    object_list = []
    for i in range(num_pop):
        seq = [random.randint(0,1) for i in range(len(vals))]
        fitness = determine_fitness(vals, weights, max_weight, seq)
        object_list.append([fitness, seq])

    return object_list


def select_parents(object_list, num_to_breed):
    ''':param object_list: List of genome lists
       :param num_pop: integer
       
       Randomly selects parents to breed in proportion to population's fitness. 
       Returns a list of integers corresponding to the selected parent's position in object_list.'''

    genomes = [i for i in range(len(object_list))]
    sum_of_fitnesses = sum_fitnesses(object_list)
    print("Sum of all fitnesses: {0}".format(sum_of_fitnesses))  

    parents = []
    if sum_of_fitnesses > 0:
        breeding_weights = [object_list[i][0]/sum_of_fitnesses for i in range(len(object_list))]
        print(breeding_weights)
        parents = random.choices(population=genomes, weights=breeding_weights, k=num_to_breed)
    else:
        parents = random.choices(population=genomes, k=num_to_breed)

    return parents


def crossover(parent_list, object_list, vals, weights, max_weight):
    ''':param parent_list: List of integers
       :param object_list: List of genome lists
       :param vals: List of integers
       :param weights: List of integers
       :param max_weight: integer
       
       Performs crossover between parents chosen from the population. Returns a list of "children" produced 
       from the crossover.'''
    list_of_children = []
    for i in range(0, len(parent_list), 2):
        seq1 = object_list[parent_list[i]][1]
        seq2 = object_list[parent_list[i+1]][1]

        crossover_pt = random.randint(0, len(seq1) - 2)
        child_1 = []
        child_2 = []
        for j in range(len(seq1)):
            if j <= crossover_pt:
                child_1.append(seq1[j])
                child_2.append(seq2[j])
            else:
                child_1.append(seq2[j])
                child_2.append(seq1[j])
        fitness_1 = determine_fitness(vals, weights, max_weight, child_1)
        fitness_2 = determine_fitness(vals, weights, max_weight, child_2)
        
        list_of_children.append([fitness_1, child_1])
        list_of_children.append([fitness_2, child_2])
        print("\nCrossover point: {0}".format(crossover_pt))
        print("Children of {0} and {1}:\n{2}\n{3}".format(parent_list[i], parent_list[i+1], child_1, child_2))

    return list_of_children


def mutate(list_of_children, prob_of_mutation, vals, weights, max_weight):
    ''':param list_of_children: List of genome lists
       :param prob_of_mutation: float between 0.0 and 1.0
       :param vals: List of integers
       :param weights: List of integers
       :param max_weight: integer
       
       Takes in a list of child genomes, the probability of mutation occurring, the list of values, the list of 
       weights, and the maximum weight the knapsack can hold. Iterates through the list of children and randomly
       chooses whether to mutate or not (in proportion to prob_of_mutation). If so, it randomly chooses a place in
       the sequence to mutate (1 => 0 or 0 => 1) and updates its fitness value to reflect the change made. Returns
       list_of_children back to the calling routine.'''

    for i in range(len(list_of_children)):
        coin_flip = random.choices(population=[0,1], weights=[prob_of_mutation, 1-prob_of_mutation], k=1)
        if coin_flip[0] == 1:
            seq = list_of_children[i][1]
            mutation_pt = random.randint(0, len(seq) - 1)
            if seq[mutation_pt] == 1:
                seq[mutation_pt] = 0
            else:
                seq[mutation_pt] = 1
            fitness = determine_fitness(vals, weights, max_weight, seq)
            list_of_children[i][0] = fitness
            list_of_children[i][1] = seq
            print("\nChild {0} has been mutated.\nUpdated sequence: {1}\nUpdated fitness: {2}".format(i, list_of_children[i][1], list_of_children[i][0]))
    
    return list_of_children



def main():
    vals = [3, 5, 8, 10]             # The values of the items
    weights = [45, 40, 50, 90]       # The weights of the items
    num_pop = 3                      # Number of genomes in population
    num_iter = 100                   # Number of times to iterate the algorithm
    max_weight = 100                 # Maximum weight allowed in knapsack
    num_to_breed = 2                 # The number of parents chosen for reproduction
    prob_of_mutation = 0.5           # The probability of a mutation occurring

    object_list = create_genome_population(vals, weights, max_weight, num_pop)
    
    for i in range(len(object_list)):
        print("Genome #{0}:".format(i))
        print("Sequence: {0}".format(object_list[i][1]))
        print("Fitness: {0}".format(object_list[i][0]))

    parent_list = select_parents(object_list, num_to_breed)
    print("Parents selected: {0}".format(parent_list))
    random.shuffle(parent_list)

    list_of_children = crossover(parent_list, object_list, vals, weights, max_weight)
    print("List of children: {0}".format(list_of_children))

    list_of_children = mutate(list_of_children, prob_of_mutation, vals, weights, max_weight)

    


if __name__ == '__main__':
    main()