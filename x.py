import matplotlib.pyplot as plt
labels = {'1':'Lake District', '2':'Scotland', '3':'Slovenia', '4':'Montenegro'}
data = [(0, 3, 0),(2, 1, 0),(3, 0, 0),(1, 2, 0),]

condensed = [x-y for x,y,z in data]
names = [labels[key] for key in labels]

plt.bar(names,condensed)
plt.ylabel("Pairwise wins - pairwise losses")
plt.show()
