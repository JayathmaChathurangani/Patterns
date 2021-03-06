import matplotlib.pyplot as plt
import csv
import sys

dataset_1 = sys.argv[1]
dataset_2 = sys.argv[2]
dataset_3 = sys.argv[3]
dataset_4 = sys.argv[4]
category_1 = sys.argv[5]
category_2 = sys.argv[6]
category_3 = sys.argv[7]
category_4 = sys.argv[8]
plot_title = sys.argv[9]

x1=[]
y1=[]

x2=[]
y2=[]

x3=[]
y3=[]

x4=[]
y4=[]

with open(dataset_1, 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(int(row[0]))
        y1.append(float(row[4]))
		
with open(dataset_2, 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(int(row[0]))
        y2.append(float(row[4]))
		
with open(dataset_3, 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append(int(row[0]))
        y3.append(float(row[4]))

with open(dataset_4, 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x4.append(int(row[0]))
        y4.append(float(row[4]))

plt.plot(x1,y1, marker='o')
plt.plot(x2,y2, marker='o')
plt.plot(x3,y3, marker='o')
plt.plot(x4,y4, marker='o')

plt.title(plot_title)

plt.legend([category_1, category_2, category_3, category_4])

plt.xlabel('Concurrency')
plt.ylabel('90 Percentile')

plt.show()
