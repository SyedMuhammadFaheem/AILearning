#Task 1
import random
import string
import numpy as np

def sort_fitness(queue_heuristic,queue_str_ind):
    temp1=np.array(queue_heuristic)
    temp2=np.array(queue_str_ind)
    sort=np.argsort(temp1)
    queue_heuristic=list(temp1[sort])
    queue_str_ind=list(temp2[sort])
    return queue_heuristic,queue_str_ind

def cal_fitness(queue_heuristic,target):
    fitness=0
    s1=len(population)-2
    s2=len(population)-1
    for i in range(len(population[s1])):
        if target[i]!=population[s1][i]:
            fitness+=1
    queue_heuristic.append(fitness)
    fitness=0
    for i in range(len(population[s2])):
        if target[i]!=population[s2][i]:
            fitness+=1
    queue_heuristic.append(fitness)
    return queue_heuristic

def mutate(individual):
    index = random.randint(0, len(target)-1)
    new_char = random.choice(genes)
    return individual[:index] + new_char + individual[index+1:]


def crossover(queue_str_ind,queue_heuristic,target):
    str1=population[queue_str_ind[0]]
    str2=population[queue_str_ind[1]]
    point = random.randint(1, len(target)-1)
    new_str1=str1[:point]+str2[point:]
    new_str2=str2[:point]+str1[point:]
    
    #mutation
    if random.random()<0.1:
        new_str1=mutate(new_str1)
    if random.random()<0.1:
        new_str2=mutate(new_str2)
               
    population.append(new_str1)
    queue_str_ind.append(len(population)-1)
    population.append(new_str2)
    queue_str_ind.append(len(population)-1)
    queue_heuristic=cal_fitness(queue_heuristic,target)
    return queue_heuristic,queue_str_ind

def genetic_solve(population,target):
    queue_heuristic=[]
    queue_str_ind=[]
    for i in range(len(population)):
        fitness=0
        for j in range(len(population[i])):
            if target[j]!=population[i][j]:
                fitness+=1
        queue_heuristic.append(fitness)
        queue_str_ind.append(i)
       
    #sorting in ascending order wrt heuristic
    queue_heuristic,queue_str_ind=sort_fitness(queue_heuristic,queue_str_ind)   
    count=0
    while target!=population[queue_str_ind[0]]:
        queue_heuristic,queue_str_ind=crossover(queue_str_ind,queue_heuristic,target)
        queue_heuristic,queue_str_ind=sort_fitness(queue_heuristic,queue_str_ind)
        length=len(queue_str_ind)
        queue_str_ind=queue_str_ind[0:2]
        queue_heuristic=queue_heuristic[0:2]
        print(population[queue_str_ind[0]],len(target)-queue_heuristic[0])
        count+=1
    print('Target String found at',count,'iterations!')
    

target='Artificial Intelligence Lab'
genes='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*(),.?'
population=[]
size=70
while len(population)<=size:
    population.append(''.join(random.choice(genes) for i in range(len(target))))
genetic_solve(population,target)