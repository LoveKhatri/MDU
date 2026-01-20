import tensorflow as tf
from tensorflow.keras import layers, models, datasets, losses
import matplotlib.pyplot as plt

# 1. Load MNIST Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# 2. Preprocessing
# Normalize to [0, 1] range
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Expand dimensions to (28, 28, 1) as required by CNNs
train_images = tf.expand_dims(train_images, 3)
test_images = tf.expand_dims(test_images, 3)

# 3. Build LeNet-5 Architecture
# Structure: Conv -> AvgPool -> Conv -> AvgPool -> Flatten -> Dense -> Dense -> Output
model = models.Sequential()

# Layer 1: Convolutional (6 filters, 5x5 kernel, Tanh activation)
model.add(layers.Conv2D(6, kernel_size=(5, 5), strides=1, activation='tanh', 
                        input_shape=(28, 28, 1), padding='same'))

# Layer 2: Average Pooling (Subsampling)
model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=2, padding='valid'))

# Layer 3: Convolutional (16 filters, 5x5 kernel, Tanh activation)
model.add(layers.Conv2D(16, kernel_size=(5, 5), strides=1, activation='tanh', padding='valid'))

# Layer 4: Average Pooling
model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=2, padding='valid'))

# Layer 5: Convolutional (120 filters, 5x5 kernel, Tanh activation)
# Note: With valid padding on previous layers, the image size is now 5x5, 
# so a 5x5 kernel here acts like a fully connected layer
model.add(layers.Conv2D(120, kernel_size=(5, 5), strides=1, activation='tanh', padding='valid'))

# Layer 6: Flatten to 1D vector
model.add(layers.Flatten())

# Layer 7: Fully Connected (84 neurons, Tanh)
model.add(layers.Dense(84, activation='tanh'))

# Layer 8: Output Layer (10 classes, Softmax)
model.add(layers.Dense(10, activation='softmax'))

# 4. Compile the Model
model.compile(optimizer='adam',
              loss=losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

# Print Model Summary to verify shapes (LeNet typically has ~60k parameters)
model.summary()

# 5. Train the Model
print("\nTraining LeNet-5...")
history = model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.1)

# 6. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nLeNet-5 Test Accuracy: {test_acc*100:.2f}%")

# 7. Visualization
# Plot accuracy history
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('LeNet-5 Accuracy on MNIST')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()