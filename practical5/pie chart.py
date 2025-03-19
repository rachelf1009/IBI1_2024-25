import matplotlib.pyplot as plt#import functions in python
#create two directories
uk_countries=[57.11,3.13,1.91,5.45]
china_provinces=[41.88,45.28,61.27,85.15]
sorted_uk = sorted(uk_countries)      
sorted_china = sorted(china_provinces) 
print(sorted_uk)
print(sorted_china)

#plot figure one using directory one

labels= "England","Wales","Northern Ireland","Scotland"#define the lables of pie chart
sizes= [57.11,3.13,1.91,5.45]#define the sizes of the pie chart
plt.pie(sizes, labels=labels, autopct="%1.1f%%", shadow= False, startangle=90,colors= ["plum", "orchid", "m", "purple"] )#plot the pie chart elaborately
plt.axis("equal")#guarantee the chart to be round
plt.show()

#plot figure 2 using directory two

labels1="Fujian","Jiangxi","Anhui","Jiangsu"#define the lables of pie chart
sizes1=[41.88,45.28,61.27,85.15]#define the sizes of the pie chart
plt.pie(sizes1, labels=labels1,autopct="%1.1f%%",shadow=False,colors = ["lightblue","lightskyblue","dodgerblue","steelblue"])#plot the pie chart elaborately
plt.axis("equal")#guarantee the chart to be round

plt.show()