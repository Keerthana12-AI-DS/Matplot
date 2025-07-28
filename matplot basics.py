import matplotlib.pyplot as plt 


## BAR PLOT


x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

# creating error
x_error = 0.5
y_error = 0.3

# plotting graph
plt.plot(x, y)
plt.errorbar(x, y, 
             yerr = y_error, 
             xerr = x_error, 
             fmt ='^')

plt.show()


##LINE GRAPH

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', linestyle='-')

# Add annotations
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

plt.title('Line Chart with Annotations')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.grid(True)
plt.show()

import numpy as np


x = np.array([1, 2, 3, 4])
y = x*2

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Any suitable title")

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
plt.plot(x1, y1, '-.')
plt.show()



##BAR CHART

import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [400, 350, 300, 450]

plt.barh(fruits, sales)

plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()


#2.multiple bar chart


import numpy as np 
import matplotlib.pyplot as plt 

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8)) 

IT = [12, 30, 1, 8, 22] 
ECE = [28, 6, 16, 5, 10] 
CSE = [29, 3, 24, 25, 17] 

br1 = np.arange(len(IT)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

plt.bar(br1, IT, color ='r', width = barWidth, 
        edgecolor ='grey', label ='IT') 
plt.bar(br2, ECE, color ='g', width = barWidth, 
        edgecolor ='grey', label ='ECE') 
plt.bar(br3, CSE, color ='b', width = barWidth, 
        edgecolor ='grey', label ='CSE') 

plt.xlabel('Branch', fontweight ='bold', fontsize = 15) 
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(IT))], 
        ['2015', '2016', '2017', '2018', '2019'])

plt.legend()
plt.show()

#3.stacked

# Data (x-axis categories)
categories = ['A', 'B', 'C']
# Stack 1
values1 = np.array([10, 20, 15])
# Stack 2
values2 = np.array([5, 12, 8])

# X positions
x = np.arange(len(categories))

# Plot
plt.bar(x, values1, label='Part 1')
plt.bar(x, values2, bottom=values1, label='Part 2')

# Labels
plt.xticks(x, categories)
plt.legend()
plt.show()


##SCATTER PLOT

#1

x = np.array([3, 12, 9, 20, 5, 18, 22, 11, 27, 16])
y = np.array([95, 55, 63, 77, 89, 50, 41, 70, 58, 83])

a = [20, 50, 100, 200, 500, 1000, 60, 90, 150, 300] # size
b = ['red', 'green', 'blue', 'purple', 'orange', 'black', 'pink', 'brown', 'yellow', 'cyan'] # color

plt.scatter(x, y, s=a, c=b, alpha=0.6, edgecolors='w', linewidth=1)
plt.title("Scatter Plot with Varying Colors and Sizes")
plt.show()

#2

x = np.random.randint(50, 150, 100)
y = np.random.randint(50, 150, 100)
colors = np.random.rand(100)  # Random float values for color mapping
sizes = 20 * np.random.randint(10, 100, 100)

plt.scatter(x, y, c=colors, s=sizes, cmap='viridis', alpha=0.7)
plt.colorbar(label='Color scale')
plt.title("Scatter Plot with Colormap and Colorbar")
plt.show()


## HISTOGRAM


import seaborn as sns

# Generate random data for the histogram
data = np.random.randn(1000)

# Creating a customized histogram with a density plot
sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Customized Histogram with Density Plot')

# Display the plot
plt.show()


##PIE CHART


# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)

# show plot
plt.show()
