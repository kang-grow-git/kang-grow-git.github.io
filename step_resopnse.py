import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

zeta = 0.3
wn = 1.0

system = signal.TransferFunction([wn**2], [1, 2*zeta*wn, wn**2])
t, y = signal.step(system)

plt.plot(t, y)
plt.title("Step Response (zeta=0.3)")
plt.xlabel("Time")
plt.ylabel("Output")
plt.grid()

plt.savefig("step_response_0303.png")
plt.show()