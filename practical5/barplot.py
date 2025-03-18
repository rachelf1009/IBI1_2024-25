language = {"JavaScript":62.3, "HTML": 52.9, "Python": 51, "SQL":51, "TypeScript": 38.5}
import matplotlib.pyplot as plt
N = 5
x = list(language.keys())
y = list(language.values())
width = 0.5
p1 = plt.bar(x,y,color = "red")
plt.ylabel("Population")
plt.title("language population") 
plt.xlabel("language")
plt.show()