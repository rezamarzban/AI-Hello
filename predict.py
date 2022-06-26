import cv2
import numpy as np
import tensorflow as tf

file = input("Enter the image file name which consists of a digit number:")

#Load previously saved AI neural network model which was created by neurons-model code.
model = tf.keras.models.load_model("handwritten.model")

#Read image from file.
img = cv2.imread(file)
#Resize image to 28×28 pixels and convert it to gray mode.
img = cv2.resize(img, (28, 28))[:,:,0]
#Invert image pixels gray color.
img = np.invert(np.array([img]))

#CLI image viewer
for i in range(0, 28):
	print('')
	for j in range(0, 28):
		print('\x1b[38;2;%d;80;180m'%img[0,i,j]+'$'+'\x1b[0m', end='')
print('')

#Predicting digit in the image by AI neural network.
prediction = model.predict(img)

#Print the most (max) match.
print(f"the digit number in the image may be a {np.argmax(prediction)}")
