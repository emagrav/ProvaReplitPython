print ("*****numpy esempio.PY*******")
import matplotlib.pyplot as plt
import numpy as np
'''
x=np.arange(0,10,2)
y=x**2+5
plt.plot(x,y)
'''

jobs="primo secondo terzo".split()
color="blu red green".split()
index=np.arange(len(jobs))

plt.bar(0,31, label='uno')
plt.bar(1,55, label='due')
plt.bar(2,110, label='tre')

plt.legend(loc='lower right')
loc='lower right'
plt.title("bello")

'''
x=np.linspace(0.,10.,50)
y = np.sin(x)

plt.plot(x,y, marker = 'o', color='red')
plt.title("seno")
plt.xlabel('X')
plt.ylabel('Y')
'''
plt.show()
