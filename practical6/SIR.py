#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
beta = 0.3 #define the infected rate
gamma = 0.05 #define the recovery rate
N = 10000#the total number of the population
S = N-1#susceptible population
I = 1#infected population that starts with one
R=0#recovery population that starts with zero


#create new list that holds the initial data
suspectible =[S]
infected =[I]
recovered=[R]

#conduct for loop to randomly infected a crowd of people and randomly recovered a crowd of people based on beta and gamma.
for i in range (1000):
    infectious_rate =beta *I/N
    I1=np.random.choice(range(2),S,p=[1-infectious_rate,infectious_rate]).sum()
    recovery_rate = gamma
    R1=np.random.choice(range(2),I,p=[1-recovery_rate,recovery_rate]).sum()
    I=I+I1-R1 #new I equals to original I adds new infected and minus recovered population
    R+=R1 #new R equals to the recovered population
    S=N-I-R #new S equals to the total number N minus new I and new R
    #append the susceptible infected and recovered list
    suspectible.append(S)
    infected.append(I)
    recovered.append(R)


#plot the figure and define the figure size
plt.figure(figsize=(6,4),dpi=150)
#respectively plot SIR list
plt.plot(suspectible,label="susceptible")
plt.plot(infected,label="infected")
plt.plot(recovered,label="recovered")
#define the labels and titles
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()

#save the plot as png to the directory
plt.savefig('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical6/SIR.png')
plt.show()

