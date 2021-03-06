# -*- coding: utf-8 -*-
"""PyStanでのHello World.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S9TIGz7fl3iyxrafACqMo7nZvtBK_wwW
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import pystan
# %matplotlib inline

plt.style.use("ggplot")

df = pd.read_excel("./data/data.xlsx")

df.head()

plt.hist(df[0])

stan_model = """
data {
  int N;
  real Y[N];
}

parameters {
  real mu;
  real<lower=0> sigma;
}

model {
  for (i in 1:N){
    Y[i] ~ normal(mu, sigma);
  }
}
"""

sm = pystan.StanModel(model_code=stan_model)

stan_data = {"N":df.shape[0], "Y":df[0]}

fit = sm.sampling(data=stan_data, iter=2000, chains = 3, warmup= 500, seed=123)

fit

fig = fit.plot()

