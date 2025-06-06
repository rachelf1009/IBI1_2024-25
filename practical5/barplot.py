
#create my own directory and input the data
language = {"JavaScript":62.3, "HTML": 52.9, "Python": 51, "SQL":51, "TypeScript": 38.5}
print(language)

#define the query variable and print the corresponding output.
input_language=input('Please enter the language you use:')
if input_language in language:
    print(f"The percentage of developers using {input_language} is {language[input_language]}%")
else:
    print(f"{input_language} is not in the dictionary")

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
plt.ylabel("Population")
plt.show()