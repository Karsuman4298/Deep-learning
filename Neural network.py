import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

nn1 = Sequential([
    Input(shape=(10,)),
    Dense(1024, activation='relu'),
    Dense(512,activation='relu'),
     Dense(128,activation='relu'),
     Dense(128,activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])
nn1.summary()
