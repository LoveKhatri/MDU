import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import matplotlib.pyplot as plt
import numpy as np

# 1. Load Fashion MNIST Dataset
# This dataset contains 60,000 images of clothing items (T-shirts, trousers, bags, etc.)
(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data()

# 2. Preprocessing
# Reshape to (Batch, Height, Width, Channels) and Normalize
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255.0
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255.0

# Class names for visualization
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 3. Build CNN with Padding & Batch Normalization
model = models.Sequential()

# Layer 1: Conv2D with 'same' padding (output size = input size)
model.add(layers.Conv2D(32, (3, 3), padding='same', input_shape=(28, 28, 1)))
model.add(layers.BatchNormalization())  # Normalize activations
model.add(layers.Activation('relu'))    # Activation applied after Batch Norm
model.add(layers.MaxPooling2D((2, 2)))

# Layer 2: Conv2D with 'same' padding
model.add(layers.Conv2D(64, (3, 3), padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Layer 3: Conv2D with 'same' padding
model.add(layers.Conv2D(128, (3, 3), padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Flatten and Dense Output
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 4. Compile the Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train the Model
print("Training on Fashion MNIST...")
history = model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.2)

# 6. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nFinal Test Accuracy: {test_acc*100:.2f}%")

# 7. Visualization
predictions = model.predict(test_images)

plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28, 28), cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions[i])
    true_label = test_labels[i]
    color = 'blue' if predicted_label == true_label else 'red'
    plt.xlabel(f"{class_names[predicted_label]}", color=color)

plt.suptitle("First 5 Predictions (Blue=Correct, Red=Incorrect)")
plt.show()