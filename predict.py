import cv2
import numpy as np
import tensorflow as tf

file = input("Enter the image file name which consists of a digit number:")

model = tf.keras.models.load_model("handwritten.model")

img = cv2.imread(file)
img = cv2.resize(img, (28, 28))[:,:,0]
img = np.invert(np.array([img]))
prediction = model.predict(img)
print(f"the digit number in the image may be a {np.argmax(prediction)}")
