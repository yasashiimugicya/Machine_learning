# -*- coding: utf-8 -*-
"""ベイズ更新.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x5T6ugINbc8NwXQYtqnCO5irARsiCaJC
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np
import pandas as pd
# %matplotlib inline

plt.style.use("ggplot")

p_a = 3.0 / 10.0
p_b = 5.0 / 9.0
p_prior = 0.5
#0:blue, 1:red
data = [0,1,0,0,1,1,1]

N_data = 7
likehood_a = bernoulli.pmf(data[:N_data], p_a)
likehood_b = bernoulli.pmf(data[:N_data], p_b)

likehood_a

pa_posterior = p_prior
pb_posterior = p_prior
pa_posterior *= np.prod(likehood_a)
pb_posterior *= np.prod(likehood_b)
norm = pa_posterior + pb_posterior
df = pd.DataFrame([pa_posterior/norm, pb_posterior/norm], columns=["post"])
x = np.arange(df.shape[0])
plt.bar(x,df["post"])
plt.xticks(x,["a","b"])

