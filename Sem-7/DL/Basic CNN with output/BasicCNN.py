import tensorflow as tf
from keras import layers, models
import matplotlib.pyplot as plt

# 1. Load and Preprocess Data
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape to (28, 28, 1) for grayscale channel and Normalize
train_images = train_images.reshape((60000, 28, 28, 1)) / 255.0
test_images = test_images.reshape((10000, 28, 28, 1)) / 255.0

# 2. Build the CNN Model
model = models.Sequential()

# First Convolutional Block
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28,1)))
model.add(layers.MaxPooling2D((2, 2)))

# Second Convolutional Block
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Classification Head
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax')) # Output layer

# 3. Compile
model.compile(optimizer='adam',
			  loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Print Summary to show architecture
model.summary()

# 4. Train
print("\nStarting CNN Training...")
history = model.fit(train_images, train_labels, epochs=5,
validation_data=(test_images, test_labels))

# 5. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nTest Accuracy: {test_acc*100:.2f}%")

# --- Visualization ---
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.9, 1])
plt.legend(loc='lower right')
plt.title('CNN Training Performance')
plt.show()