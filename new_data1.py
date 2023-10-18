import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import numpy as np
import pandas as pd

loaded_model = load_model("my_model.h5")

# Defining and preprocessing
new_data = {
    'Time': ["0:00:26"],
    'Reading ID': [14],
    'Humidity': [38.3],
    'Temperature': [21.9],
    'MQ139': [69],
    'TVOC': [0],
    'eCO2': [400],
}

df = pd.DataFrame(new_data)

time_data = pd.to_datetime(df['Time'], format='%H:%M:%S')

total_seconds = time_data.dt.hour * 3600 + time_data.dt.minute * 60 + time_data.dt.second

df['Time'] = total_seconds.astype('float32')


predictions = loaded_model.predict(df)

print(predictions)



