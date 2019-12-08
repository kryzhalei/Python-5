import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0,200); 
sin = np.sin
cos = np.cos
tan = np.tan
pi = np.pi
x = input('Input: ')
x = eval(x)
ys = np.array([])


ctr = 0
for k in n:
    if ctr == 0:
        y = -1.5*x[ctr] + 2*x[ctr+1] - 0.5*x[ctr+2]
        ys = np.append(ys,y)
        ctr = ctr + 1
    elif ctr>0 and ctr<199:
        y = 0.5*x[ctr+1] - 0.5*x[ctr-1]
        ys = np.append(ys,y)
        ctr = ctr + 1
    else:
        y = 1.5*x[ctr] - 2*x[ctr-1] + 0.5*x[ctr-2]
        ys = np.append(ys,y)
plt.plot(n,ys,n,x)