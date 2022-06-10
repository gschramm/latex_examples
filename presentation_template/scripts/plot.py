import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Roboto'

fig, ax = plt.subplots()
ax.plot([1,2,3],[1,4,9],'.-')
ax.set_xlabel('x [keV]')
ax.set_ylabel('y [mm]')
ax.set_title('test plot')
ax.grid(ls = ':')
fig.tight_layout()
fig.savefig('plot.pdf')
fig.show()
