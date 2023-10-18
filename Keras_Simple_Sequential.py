# -*- coding: utf-8 -*-
"""son_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-t1dnvVK3UJRm1sAGo0Gjhd42sMcgs5L

**Kütüphanelerin ve veri setinin yüklenmesi (Çalıştırmak için öncelikle dosyanın Colab'ta bulunması gerekiyor. Soldaki panelden halledilebilir.)**
"""

import tensorflow as tf
from keras.utils import to_categorical
from keras.models import load_model
import pandas as pd
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('electrical_1.csv')

dataset.columns = dataset.columns.str.strip()
dataset.drop(['Detector'], axis=1, inplace=True)

x = dataset.drop(columns=["Status", "Time", "Reading ID"])

print(x)
x.shape

y = dataset["Status"]
print(y)
y.shape

#from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#import tensorflow as tf
#from keras.utils import to_categorical

y_train_encoded = to_categorical(y_train)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(256, input_shape=(None, 5), activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train_encoded, epochs=100)

y_test_encoded = to_categorical(y_test)
print(y_test_encoded)
y_test_encoded.shape

model.evaluate(x_test, y_test_encoded)

model.save('new_model.keras')

model.save("new_model.h5")

#from keras.models import load_model

# Load the saved model
#loaded_model = load_model("my_model.h5")

#predictions = model.predict(new_data)

#print(predictions)

#New data için olan kısım diğer programlarda bulunabilir