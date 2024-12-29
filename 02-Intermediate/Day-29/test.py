import numpy as np
from tensorflow.keras.models import load_model
from load_data import X_test
import matplotlib.pyplot as plt

model = load_model('D:/45-Days-Challege-JS-Python/Python/Learning-Projects/Python-45-Days-Project-Challenge/02-Intermediate/Day-29/unet_model.h5')

image = X_test[0]

predicted_mask = model.predict(image.reshape(1, 32, 32, 3))[0]

predicted_mask = (predicted_mask > 0.5).astype(np.uint8)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Predicted Mask")
plt.imshow(predicted_mask.squeeze(), cmap='gray')

plt.show()
