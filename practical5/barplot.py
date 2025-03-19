
#create my own directory and input the data
language = {"JavaScript":62.3, "HTML": 52.9, "Python": 51, "SQL":51, "TypeScript": 38.5}
#begin to draw pictures
import matplotlib.pyplot as plt
#define x and y axis
x = list(language.keys())
y = list(language.values())
#define the width of the bar chart
width = 0.5
#plot the bar chart
plt.bar(x,y,color = ["thistle", "plum", "orchid", "m", "purple"])

#label the name of x and y axis and the title
plt.title("language population") 
plt.xlabel("language")

plt.show()
plt.ylabel("Population")