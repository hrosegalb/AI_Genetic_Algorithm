from genome import Genome
import random


def sum_fitnesses(object_list):
    ''':param object_list: List of Genome objects
       
       Sums the fitnesses of each genome in the list and returns the value.'''
    return sum([object_list[i].get_fitness() for i in range(len(object_list))])


def main():
    vals = [3, 5, 8, 10]
    weights = [45, 40, 50, 90]
    num_pop = 6
    num_iter = 100
    max_weight = 100

    object_list = []
    for i in range(num_pop):
        seq = [random.randint(0,1) for i in range(len(vals))]
        genome = Genome(seq)
        genome.determine_fitness(vals, weights, max_weight)
        object_list.append(genome)
    
    for i in range(len(object_list)):
        print("Genome #{0}:".format(i))
        object_list[i].print()

    sum_of_fitnesses = sum_fitnesses(object_list)
    print("Sum of all fitnesses: {0}".format(sum_of_fitnesses))

    breeding_weights = [object_list[i].get_fitness()/sum_of_fitnesses for i in range(len(object_list))]
    print(breeding_weights)

    genomes = [i for i in range(len(object_list))]
    parents = random.choices(genomes, breeding_weights, k=num_pop)
    print("Parents selected: {0}".format(parents))


 




if __name__ == '__main__':
    main()