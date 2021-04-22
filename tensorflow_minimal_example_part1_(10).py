# -*- coding: utf-8 -*-
"""TensorFlow_Minimal_example_Part1 (10).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ybFPRTmVTdIy6JQS8-xe72Jzg4-88Zcp

# TensorFlow 2.0

## ライブラリのインポート
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

"""## データの作成"""

observations = 1000

xs = np.random.uniform(low=-10, high=10, size=(observations,1))
zs = np.random.uniform(-10, 10, (observations,1))

generated_inputs = np.column_stack((xs,zs))

noise = np.random.uniform(-1, 1, (observations,1))

generated_targets = 2*xs - 3*zs + 5 + noise

np.savez('TF_intro', inputs=generated_inputs, targets=generated_targets)