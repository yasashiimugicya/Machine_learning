# -*- coding: utf-8 -*-
"""ロジスティック回帰.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tXGsEAF-CIN8EPhQJKGeqbVh-GOMQ44_
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pystan
from scipy.stats import mstats
# %matplotlib inline

plt.style.use("ggplot")

df = pd.read_excel("./data/dose_response.xlsx")

df.head()

plt.scatter(df["log10 C"], df["death"])

stan_model = """
data {
  int N;
  real X[N];
  int<lower=0, upper=1> Y[N];
}

parameters {
  real a;
  real b;
}

model {
  for (n in 1:N){
    Y[n] ~ bernoulli_logit(a * X[n] + b);
  }
}

"""

sm = pystan.StanModel(model_code= stan_model)

stan_data = {"N":df.shape[0], "X":df["log10 C"], "Y":df["death"]}

fit = sm.sampling(data = stan_data, iter = 2000, warmup=500, chains=3, seed=123)

fit

a, b = 13.57, -20.27

fig = fit.plot()

ms_a = fit.extract("a")["a"]
ms_b = fit.extract("b")["b"]

x = np.arange(1.0, 2.0, 0.01)
f = lambda x : 1.0 / (1.0 + np.exp(-x))
df_b = pd.DataFrame([])
for i in range(x.shape[0]):
    df_b[i] = f(ms_a * x[i] + ms_b)

df_b.head()

low_y50, high_y50 = mstats.mquantiles(df_b, [0.25, 0.75], axis=0)
low_y95, high_y95 = mstats.mquantiles(df_b, [0.025, 0.975], axis=0)

plt.scatter(df["log10 C"], df["death"])
plt.fill_between(x, low_y95, high_y95, alpha = 0.3, color = "gray")
plt.fill_between(x, low_y50, high_y50, alpha = 0.6, color = "darkgray")
plt.plot(x, f(a*x+b))

