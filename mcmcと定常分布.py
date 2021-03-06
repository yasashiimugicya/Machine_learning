# -*- coding: utf-8 -*-
"""MCMCと定常分布.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13TGK3AwUlGnemyiueXCBUimzMO5P1Nyc
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline

plt.style.use("ggplot")
np.random.seed(123)

p_trans = np.zeros([3,3])

#0:office, 1:kyukei, 2:jikken
p_trans[0,0] = 0.1
p_trans[0,1] = 0.2
p_trans[0,2] = 0.7
p_trans[1,0] = 0.1
p_trans[1,1] = 0.4
p_trans[1,2] = 0.5
p_trans[2,0] = 0.3
p_trans[2,1] = 0.3
p_trans[2,2] = 0.4

p_trans

NMCS = 400
c_state = 0
c_arr = [c_state]
for i in range(NMCS):
    current = np.random.choice(3,1,p=p_trans[c_state, :])
    c_state = current[0]
    c_arr.append(c_state)
df = pd.DataFrame(c_arr)

c_state = 0
np.random.choice(3,1,p=p_trans[c_state, :])

df.head()

plt.plot(df[0])
plt.xlabel("MCS")
plt.ylabel("place")

plt.hist([df[0][:10], df[0][:50], df[0][:200], df[0][:400]], normed=True, label=["10","50","200","400"])
plt.xlabel("place")
plt.ylabel("frequency")
plt.legend()

