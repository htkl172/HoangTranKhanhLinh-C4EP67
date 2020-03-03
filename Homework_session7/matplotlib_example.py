import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

#1 Prepare data
machine_types = [18, 4, 2 ]

#2 Prepare label
machine_names = ['PC', 'MAC', 'Linux']

#3 Draw pie
pyplot.pie(machine_types, labels = machine_names, autopct = '%.1f%%', shadow = True, explode = [0, 0.2, 0])
pyplot.title('PC vs MAC vs Linux percentage')
pyplot.axis('equal')

#4 Show
pyplot.show()