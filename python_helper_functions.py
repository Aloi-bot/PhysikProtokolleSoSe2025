import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import statistics

data = []

#Read data
# Dateiname einlesen
file_name = ''
if os.access(file_name, os.R_OK) == False:
    print('Unable to read file')

# x, y, z, ...
data_x, data_y = np.loadtxt(file_name, unpack=True, usecols=(0, 2), delimiter=',', skiprows=1)


#Statistics
statistics.mean(data_y)
statistics.stdev(data_y)


#Plotting
plot_coloumns = 2
plot_rows = 2
pos_index = 1

fig = plt.figure(figsize=(10,8)) 
fig.add_subplot(plot_coloumns, plot_coloumns, pos_index)
plt.title('Titel')
plt.ylabel('')
plt.xlabel('')
plt.plot([], [], markersize=2, label='Beschriftung')
plt.legend(loc="upper right", prop={'family': 'serif', 'size': 12})
plt.show()