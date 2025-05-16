import matplotlib.pyplot as plt
import numpy as np
import statistics

#Plotting
plot_coloumns = 1
plot_rows = 1
pos_index = 1

x_values = np.linspace()
magnification = 2



fig = plt.figure(figsize=(10,8)) 
fig.add_subplot(plot_coloumns, plot_coloumns, pos_index)
plt.title('Titel')
plt.ylabel('')
plt.xlabel('')
plt.plot([], [], markersize=2, label='Beschriftung')
plt.legend(loc="upper right", prop={'family': 'serif', 'size': 12})
plt.show()