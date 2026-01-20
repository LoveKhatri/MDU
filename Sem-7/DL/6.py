import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import matplotlib.pyplot as plt

# 1. Load and Preprocess Data
# CNNs require input shape (Batch_Size, Height, Width, Channels)
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Reshape data to include channel dimension (1 for grayscale)
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255.0
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255.0

# 2. Build the CNN Architecture
model = models.Sequential()

# First Convolutional Layer: 32 Filters, 3x3 Kernel
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
# First Pooling Layer
model.add(layers.MaxPooling2D((2, 2)))

# Second Convolutional Layer: 64 Filters, 3x3 Kernel
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# Second Pooling Layer
model.add(layers.MaxPooling2D((2, 2)))

# Flattening and Dense Layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 3. Compile the Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Train the Model
print("Training CNN Model...")
history = model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.1)

# 5. Evaluate Accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nTest Accuracy: {test_acc*100:.2f}%")

# 6. Plot Training Accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label = 'Validation Accuracy')
plt.title('CNN Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()