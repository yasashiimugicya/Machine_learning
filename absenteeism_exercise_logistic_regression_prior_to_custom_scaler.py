# -*- coding: utf-8 -*-
"""Absenteeism Exercise - Logistic Regression_prior to custom_scaler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13DRkCGH6oDWL3gnPDSphrTbt1L5PT3nN

# 欠勤率の予測

## ライブラリのインポート
"""

# 関連するライブラリをインポート
import pandas as pd
import numpy as np

"""## データの読み込み"""

# 前処理をしたCSVファイルの読み込み
data_preprocessed = pd.read_csv('Absenteeism_preprocessed.csv')

# 中身の確認
data_preprocessed.head()

"""## ターゲットの作成"""

# 'Absenteeism Time in Hours'の中央値を見つける
data_preprocessed['Absenteeism Time in Hours'].median()

# 上のコードで確認した中央値を元に、1と0に分けたターゲットを作成

# レクチャーでのはじめのコード
# targets = np.where(data_preprocessed['Absenteeism Time in Hours'] > 3, 1, 0)

# 中央値よりも大きいかどうかで1と0のターゲットを作成
targets = np.where(data_preprocessed['Absenteeism Time in Hours'] > 
                   data_preprocessed['Absenteeism Time in Hours'].median(), 1, 0)

# 中身の確認
targets

# targetを変数に代入
data_preprocessed['Excessive Absenteeism'] = targets

# 前処理したデータの確認
data_preprocessed.head()

"""## ターゲットに関して"""

# ターゲットがバランスしているか確認
# targets.sum() は1の数を示す
# the shape[0] はデータの数
targets.sum() / targets.shape[0]

# 不要な列の削除
data_with_targets = data_preprocessed.drop(['Absenteeism Time in Hours'],axis=1)

# data_with_targets is data_preprocessed = Trueであれば、二つは同じオブジェクトである
# 二つのオブジェクトが異なっていれば、チェックポイントが作成されていることを示す
data_with_targets is data_preprocessed

# データの確認
data_with_targets.head()

"""## 入力データの作成"""

data_with_targets.shape

# 14番目までの列の抽出
data_with_targets.iloc[:,:14]

# 最後の列を取り除く
data_with_targets.iloc[:,:-1]

# 入力データを変数に格納する
unscaled_inputs = data_with_targets.iloc[:,:-1]

"""## データの標準化"""

# 標準化するためのStandardScalerクラスをインポート
from sklearn.preprocessing import StandardScaler

# クラスからオブジェクトを作成
absenteeism_scaler = StandardScaler()

# unscaled_inputsをモデルにフィット
absenteeism_scaler.fit(unscaled_inputs)

# transformメソッドを使って値を標準化
scaled_inputs = absenteeism_scaler.transform(unscaled_inputs)

# データの確認
scaled_inputs

# 配列の形状の確認
scaled_inputs.shape

"""## データの分割

### ライブラリのインポート
"""

from sklearn.model_selection import train_test_split

"""### データの分割"""

train_test_split(scaled_inputs, targets)

# 訓練データとテストデータに関し、入力とターゲットに分けて変数に代入する
x_train, x_test, y_train, y_test = train_test_split(scaled_inputs, targets, #train_size = 0.8, 
                                                                            test_size = 0.2, random_state = 20)

# データの形状の確認
print (x_train.shape, y_train.shape)

# データの形状の確認
print (x_test.shape, y_test.shape)

"""## sklearnを使ったロジスティック回帰モデルの作成"""

# LogisticRegressionのインポート
from sklearn.linear_model import LogisticRegression

# 'metrics'モジュールのインポート
from sklearn import metrics

"""### モデルの訓練"""

# LogisticRegressionクラスからオブジェクトを作成
reg = LogisticRegression()

# モデルへのあてはめ
reg.fit(x_train,y_train)

# モデルの正確性の計算
reg.score(x_train,y_train)

"""### 正確性の計算の実装"""

# モデルに入れた結果の出力を変数に代入する
model_outputs = reg.predict(x_train)
model_outputs

# ターゲットの確認
y_train

# 出力とターゲットが同じかの確認
model_outputs == y_train

# 出力をターゲットが同じである数のカウント
np.sum((model_outputs==y_train))

# データの合計の数の確認
model_outputs.shape[0]

# 出力とターゲットが同じ数を合計の数で割って正確性を求める
np.sum((model_outputs==y_train)) / model_outputs.shape[0]

"""### 折半と係数"""

# 切片（バイアス）の確認
reg.intercept_

# 係数（重み）の確認
reg.coef_

# 列の名前の確認
unscaled_inputs.columns.values

# 列の名前を変数に代入
feature_name = unscaled_inputs.columns.values

summary_table = pd.DataFrame (columns=['Feature name'], data = feature_name)

summary_table['Coefficient'] = np.transpose(reg.coef_)

summary_table

summary_table.index = summary_table.index + 1

summary_table.loc[0] = ['Intercept', reg.intercept_[0]]

summary_table = summary_table.sort_index()
summary_table

"""## 係数の理解"""

summary_table['Odds_ratio'] = np.exp(summary_table.Coefficient)

summary_table

summary_table.sort_values('Odds_ratio', ascending=False)