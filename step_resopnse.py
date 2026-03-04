import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

zeta = 0.1
wn = 1.0

system = signal.TransferFunction([wn**2], [1, 2*zeta*wn, wn**2])
t, y = signal.step(system)

plt.plot(t, y)
plt.title("Step Response (zeta=0.1)")
plt.xlabel("Time")
plt.ylabel("Output")
plt.grid()

plt.savefig("step_response_0304_3.png")
plt.show()

max_value = max(y)
steady_state = 1
overshoot = (max_value - steady_state) / steady_state * 100

print("Overshoot:", overshoot, "%")

'''
index.html에 변경해서 넣기
<p>2026.03.03 - Step response 실험 완료.</p>
<img src="step_response_0303.png" width="500">

그후 깃 푸시
git add .
git commit -m "Add step response graph"
git push



Overshoot(%)= ((최대값 - 정상상태값) / 정상상태값 )​× 100
'''