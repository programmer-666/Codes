# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

city_codes = np.array([17,22,23,44])
population = np.array([512, 234, 267, 433])

plt.xlabel("City Codes")
plt.ylabel("Population")
plt.title("Graphic Title")
#plt.plot(city_codes, population, "black")
# starting
npa = np.linspace(1, 10, 100)
npa2 = np.linspace(10, 20, 100)*npa
#plt.plot(npa, npa2, 'b--') # *-
#plt.subplot(1, 2, 1) # 1 row 2 col first graphic
#plt.plot(npa, npa2, 'r--')
#plt.subplot(1, 2, 2)
#plt.plot(npa, npa2, 'b--')
cleanf = plt.figure() # a clean canvas
faxes = cleanf.add_axes([0, 0, 0.9, 0.9]) # figure axes [x start, y start, width, height]
faxes.set_xlabel("x side")
faxes.set_ylabel("y side")
#faxes.plot(npa, npa2, "g--")
# customize
f2 = plt.figure()
ax1 = f2.add_axes([0.1, 0.1, 0.6, 0.6])
ax2 = f2.add_axes([0.5, 0.2, 0.1, 0.1])
#ax1.plot(npa, npa2, "g")
#ax2.plot(npa2, npa, "b")

fg, axs = plt.subplots(nrows=1, ncols=2)
#axs[0].plot(npa, npa2)
#axs[1].plot(npa2, npa)
plt.tight_layout()
# interwined graphics
nf = plt.figure(figsize=(3,3), dpi=600)
ax1 = nf.add_axes([0.1, 0.1, 0.9, 0.9])
#ax1.plot(npa, npa2, label = "npa/npa2")
#ax1.plot(npa2, npa, label = "npa2/npa")
#ax1.legend(loc=1) # loc -> location
#nf.savefig("test.png", dpi=1200)
# subplots
na1 = np.linspace(0, 3.14, 5000)
na2 = na1**(1/2)
f, x = plt.subplots(dpi = 600)
#x.plot(na1, na2, color = '#000', alpha=0.7) # alpha -> opacity
#x.plot(na2, na1, color='#1c1c1c', linestyle = "--")
#x.plot(na1, na2**3, color='#268bd2', linewidth=3, linestyle = ":")
#x.plot(na1, na2**5, color='#333A36', linestyle = "--", marker = "o", markerfacecolor = "red", markersize=12)
# advanced
#plt.scatter(na1, na2, color = "#000")
#plt.hist(na1, na2)
plt.boxplot(na2)
# other graphics