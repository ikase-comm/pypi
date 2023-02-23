import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,5)
y = x**5
plt.plot([1,2,3,4],[10,20,30,40],"go",x,y,"r^")
plt.title("Sales Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
