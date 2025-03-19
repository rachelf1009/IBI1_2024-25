import matplotlib.pyplot as plt#import functions in python
#create two directories
uk_countries={"England":57.11,"Wales":3.13,"North Ireland":1.91,"Scotland":5.45}
china_provinces={"Zhejiang":65.77,"Fujian":41.88,"Jiangxi":45.28,"Anhui":61.27,"Jiangsu":85.15}

#plot figure one using directory one
plt.figure()
labels= list(uk_countries.keys())#define the lables of pie chart
sizes= list(uk_countries.values())#define the sizes of the pie chart
plt.pie(sizes, labels=labels, autopct="%1.1f%%", shadow= False, startangle=90,colors= ["plum", "orchid", "m", "purple"] )#plot the pie chart elaborately
plt.axis("equal")#guarantee the chart to be round

#plot figure 2 using directory two
plt.figure()
labels1=list(china_provinces.keys())#define the lables of pie chart
sizes1=list(china_provinces.values())#define the sizes of the pie chart
plt.pie(sizes1, labels=labels1,autopct="%1.1f%%",shadow=False,colors = ["lightblue","skyblue","lightskyblue","dodgerblue","steelblue"])#plot the pie chart elaborately
plt.axis("equal")#guarantee the chart to be round

plt.show()