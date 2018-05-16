import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('loadDataSo2_4.csv',usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()
