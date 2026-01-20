import os
# MUST disable oneDNN before TensorFlow imports to avoid MKL primitive errors on Windows
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras import layers, models, datasets, optimizers
import matplotlib.pyplot as plt
import numpy as np

# 1. Load MNIST Dataset (using MNIST instead of CIFAR-10 due to memory constraints)
# MNIST has 10 classes: digits 0-9
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# 2. Preprocessing
# Use subset FIRST to avoid memory issues (VGG-16 is memory-intensive)
train_images = train_images[:5000]
train_labels = train_labels[:5000]
test_images = test_images[:1000]
test_labels = test_labels[:1000]

# Convert grayscale to RGB by repeating the channel 3 times (VGG expects 3 channels)
# Resize from 28x28 to 32x32 using numpy for better memory handling
train_images_resized = []
for img in train_images:
    # Add channel dimension, tile to 3 channels, resize to 32x32
    img_3ch = np.repeat(img[:, :, np.newaxis], 3, axis=2)
    # Simple resize by padding
    img_resized = np.pad(img_3ch, ((2, 2), (2, 2), (0, 0)), mode='constant')
    train_images_resized.append(img_resized)
train_images = np.array(train_images_resized, dtype='float32') / 255.0

test_images_resized = []
for img in test_images:
    img_3ch = np.repeat(img[:, :, np.newaxis], 3, axis=2)
    img_resized = np.pad(img_3ch, ((2, 2), (2, 2), (0, 0)), mode='constant')
    test_images_resized.append(img_resized)
test_images = np.array(test_images_resized, dtype='float32') / 255.0

# One-hot encoding labels
train_labels = tf.keras.utils.to_categorical(train_labels, 10)
test_labels = tf.keras.utils.to_categorical(test_labels, 10)

# 3. Build Simplified VGG-like Architecture
# Reduced filter counts to work within memory constraints
# Still demonstrates the core VGG concept: stacked conv layers with max pooling
model = models.Sequential()

# Block 1 - Reduced from 64 to 32 filters
model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))

# Block 2 - Reduced from 128 to 64 filters
model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))

# Block 3 - Reduced from 256 to 128 filters
model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))

# Block 4 - Reduced from 512 to 256 filters
model.add(layers.Conv2D(256, (3, 3), padding='same', activation='relu'))
model.add(layers.Conv2D(256, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))

# Flatten and Fully Connected Layers
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))  # Reduced from 512
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, activation='softmax')) # 10 classes

# 4. Compile the Model
# Using Adam optimizer (more memory-efficient than SGD with momentum)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# 5. Train the Model
# Note: Using MNIST with simplified VGG-style architecture due to memory constraints
# Still demonstrates the key VGG concepts: deep stacked convolutions
print("\nTraining VGG-style CNN on MNIST...")
history = model.fit(train_images, train_labels, epochs=3, batch_size=32, validation_split=0.1)

# 6. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nVGG-style CNN Test Accuracy: {test_acc*100:.2f}%")