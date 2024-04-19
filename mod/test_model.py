from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error
import tensorflow as tf
import os
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split

# from tensorflow.keras.mod import Sequential
# from tensorflow.keras.layers import *
# from tensorflow.keras.callbacks import ModelCheckpoint
# from tensorflow.keras.losses import MeanSquaredError as MSE
# from tensorflow.keras.metrics import RootMeanSquaredError as RMSE, Accuracy, F1Score, Precision
# from tensorflow.keras.optimizers import Adam

zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True)
csv_path, _ = os.path.splitext(zip_path)

df = pd.read_csv(csv_path)
df = df[5::6] # уменьшаем количество данных
df.index = pd.to_datetime(df['Date Time'], format='%d.%m.%Y %H:%M:%S') # делаем индексом дату и время
df = df.drop(columns=['Date Time']) # удаляем лишний столбец даты и времени
df.head()

temp = df['T (degC)']
def df_to_X_y(df, window_size=5):
  df_as_np = df.to_numpy()
  X = []
  y = []
  for i in range(len(df_as_np)-window_size):
    row = [[a] for a in df_as_np[i:i+window_size]]
    X.append(row)
    label = df_as_np[i+window_size]
    y.append(label)
  return np.array(X), np.array(y)

WINDOW_SIZE = 5
X1, y1 = df_to_X_y(temp, WINDOW_SIZE)
X_test1, y_test1 = X1[65000:], y1[65000:]

model1 = load_model(r'C:\Users\Пользователь\OneDrive\Рабочий стол\MoscowMetroHack\mod\model1_7.keras')
test_predictions = model1.predict(X_test1).flatten()
test_results = pd.DataFrame(data={'Train Predictions':test_predictions, 'Actuals':y_test1})
def mse():
    return mean_squared_error(test_results['Actuals'], test_results['Train Predictions']) # Выход, который дает бот

