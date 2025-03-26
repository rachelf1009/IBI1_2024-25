#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#define the vaccination rate and create new list
V_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
#create list that contains the total number of infectious ones with different vaccintion rate
infected_all=[]

#conduct different vaccination rate
for rate in V_rate:
    #define basic parameters
    beta = 0.3 
    gamma = 0.05 
    N = 10000
    I = 1
    R=0
    V=int(N*rate)
    S=N-1-V
    S=max(S,0)#make sure S is non-negative
    infected =[I]#create infected list 
    #begin to randomly infect 1000 times
    for i in range (1000):
      #asure the I to be non-negative
      I=max(0,I)
      infectious_rate =beta *I/N
      I1=np.random.choice(range(2),S,p=[1-infectious_rate,infectious_rate]).sum()
      recovery_rate = gamma
      R1=np.random.choice(range(2),I,p=[1-recovery_rate,recovery_rate]).sum()
      #update infected and susceptible population
      I=I+I1-R1
      S=max(S-I1,0)
      #append the infected list of infected population
      infected.append(I)
    #append infected list with different vaccination rate
    infected_all.append(infected)

#define figure parameters   
plt.figure(figsize=(6,4),dpi=150)
#input index to plot V_rate list respectively
index=0
for j in infected_all:
   rate=V_rate[index]
   index +=1
   plt.plot(j,label=f'Vaccination rate: {rate*100}%',color= cm.viridis(30))

#define labels and titles
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rate")
plt.legend()
plt.show()

