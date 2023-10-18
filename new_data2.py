import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import numpy as np
import pandas as pd

loaded_model = load_model("your_model.h5")

# Defining and preprocessing
new_data = {
    'Reading ID': [0],
    'Humidity': [41.5],
    'Temperature': [22.3],
    'MQ139': [132],
    'TVOC': [5761],
    'eCO2': [5898],
}

df = pd.DataFrame(new_data)

predictions = loaded_model.predict(df)
print(predictions)



#veri = predictions.tolist()
flat_list = predictions.flatten().tolist()

print(flat_list)
print("%" + str(flat_list[0] * 100))
print("%" + str(flat_list[1] * 100))
print("%" + str(flat_list[2] * 100))
