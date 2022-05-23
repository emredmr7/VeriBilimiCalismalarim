import matplotlib.pyplot as plt
import numpy as np
'''
#1)
x = [1,2,3,4]
y = [1,4,9,16]
plt.axis([0,6,0,20]) #x ekseni 0'dan 6'ya, y ekseni 0'dan 20'ye
plt.plot(x,y, color="orange", linewidth=6)
plt.title("BAŞLIK")
plt.xlabel("x başlığı")
plt.ylabel("y başlığı")
'''
'''
#2)
x = np.linspace(0,2,100)
plt.plot(x, x, label="linear", color="red")
plt.plot(x, x**2, label="quardatic", color="blue")
plt.plot(x, x**3, label="cubic", color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("TİTLE")
plt.legend()
'''
#3
x = np.linspace(0,2,100)

fig,axs = plt.subplots(3)
axs[0].plot(x, x, color="red")
axs[0].set_title("linear")

axs[1].plot(x, x**2, color="blue")
axs[1].set_title("quadratic")

axs[2].plot(x, x**3, color="green")
axs[2].set_title("cubic")
plt.show()