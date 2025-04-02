#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
'''
make array of all susceptible population
define susceptible as 0,infected as 1
randomly choose 1 point in 100*100 as 1
plot figure
'''
population = np.zeros((100,100))
outbreak = np.random.choice ( range (100) ,2)
population [ outbreak [ 0 ] , outbreak [ 1 ] ] = 1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')


#find the coordinate of the infected one
def find_infectedpoints(population):
    return np.where(population ==1)


#find the neighbors of the infected one
def neighbors_address(x,y):
    neighbors =[]#create new list
    d =[-1,0,1]#difine the derta distance list
    for dx in d:
        for dy in d:
            if dx == 0 and dy==0:#exclude the infected point itself
                continue
            neighbors_x = x +dx
            neighbors_y = y+dy
            if 0<=neighbors_x<100 and 0<=neighbors_y<100:#neighbors point should be limited to the scale
                neighbors.append((neighbors_x,neighbors_y))
    return neighbors


#randomly infect susceptible neighbors at rate of beta
def infected_neighbors(neighbors):
    for x, y in neighbors:
            if population[x,y] == 0: 
                population[x, y] = np.random.choice(range(2),1,p=[1-beta,beta])

#ranmdomly recover infected population at rate of gamma
def recover(x, y):
    population[x,y] = np.random.choice([1,2],1,p=[1-gamma,gamma])


#difine beta and gamma and provide the times of infection
beta=0.3
gamma=0.05
times=100
for t in range(times):
    infected_x, infected_y=find_infectedpoints(population)
    for i in range(len(infected_x)):
        x=infected_x[i]
        y=infected_y[i]
        neighbors = neighbors_address(x, y)
        infected_neighbors(neighbors)
        recover(x,y)
    
    #plot different plot during different times of infection
    if t ==10 or t == 50 or t==99:
      plt.figure(figsize=(6, 4), dpi=150)
      plt.imshow(population, cmap='viridis', interpolation='nearest')     
plt.show()