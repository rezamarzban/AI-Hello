import os
import cv2
import numpy as np
import tensorflow as tf
mnist = tf.keras.datasets.mnist
                                                        (x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)     x_test = tf.keras.utils.normalize(x_test, axis=1)
                                                        model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
#Neurons
model.add(tf.keras.layers.Dense(200, activation='relu'))
model.add(tf.keras.layers.Dense(200, activation='relu'))
#The 10 digits
model.add(tf.keras.layers.Dense(10, activation='softmax'))                                                      
model.compile(optimizer='RMSprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)                   
model.save('handwritten.model')


loss, accuracy = model.evaluate(x_test, y_test)

print(loss)
print(accuracy)