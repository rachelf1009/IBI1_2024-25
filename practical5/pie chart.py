import matplotlib.pyplot as plt
uk_countries={"England":57.11,"Wales":3.13,"North Ireland":1.91,"Scotland":5.45}
china_provinces={"Zhejiang":65.77,"Fujian":41.88,"Jiangxi":45.28,"Anhui":61.27,"Jiangsu":85.15}
plt.figure()
labels= list(uk_countries.keys())
sizes= list(uk_countries.values())
plt.pie(sizes, labels=labels, autopct="%1.1f%%", shadow= False, startangle=90)
plt.axis("equal")

plt.figure()
labels1=list(china_provinces.keys())
sizes1=list(china_provinces.values())
plt.pie(sizes1, labels=labels1,autopct="%1.1f%%",shadow=False)
plt.axis ("equal")

plt.show()