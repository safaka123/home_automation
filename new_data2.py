import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import numpy as np
import pandas as pd

#Kütüphanelerden sonra ilk satırda modelin yüklenmesi gerçekleşir

loaded_model = load_model("your_model.h5")


# Yeni verinin tanımlanması
new_data = {
    'Reading ID': [0],
    'Humidity': [41.5],
    'Temperature': [22.3],
    'MQ139': [132],
    'TVOC': [5761],
    'eCO2': [5898],
}


#Pandas DataFrame yardımıyla yukarıdaki veri modelin anlayacağı dile çevrilir
df = pd.DataFrame(new_data)

#Verisetinin işlem sonucu (Array içinde array olarak düşünülebilir. 0, 1 ya da 2 olmak üzere
# yüzdelik sonuçlar elde edilir
predictions = loaded_model.predict(df)
print(predictions)

#Array içinde array olarak gelen sonuçlar bir listeye dönüştürülür ve bu sayede index olarak alınabilir
flat_list = predictions.flatten().tolist()


#Index değişkenleri ile verilere erişilir ve okuması daha kolay olduğundan yüzdelik formatta gösterilir
print(flat_list)
print("%" + str(flat_list[0] * 100))
print("%" + str(flat_list[1] * 100))
print("%" + str(flat_list[2] * 100))
