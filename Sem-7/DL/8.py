import tensorflow as tf
from tensorflow.keras import layers, models, datasets, regularizers
import matplotlib.pyplot as plt

# 1. Load Fashion MNIST Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data()

# 2. Preprocessing
# Normalize pixel values
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255.0
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255.0

# 3. Build CNN with L2 Regularization and Dropout
model = models.Sequential()

# Layer 1: Conv2D with L2 Regularization
# kernel_regularizer=regularizers.l2(0.001) applies a penalty to weights
model.add(layers.Conv2D(32, (3, 3), activation='relu', 
                        kernel_regularizer=regularizers.l2(0.001), 
                        input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Dropout Layer: Randomly drops 25% of neurons to prevent co-adaptation
model.add(layers.Dropout(0.25))

# Layer 2: Conv2D with L2 Regularization
model.add(layers.Conv2D(64, (3, 3), activation='relu', 
                        kernel_regularizer=regularizers.l2(0.001)))
model.add(layers.MaxPooling2D((2, 2)))

# Dropout Layer: Higher dropout rate (30%) deeper in the network
model.add(layers.Dropout(0.3))

# Flatten and Dense Layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
model.add(layers.Dropout(0.4)) # Heavy dropout before final classification
model.add(layers.Dense(10, activation='softmax'))

# 4. Compile the Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train the Model
print("Training Regularized CNN...")
history = model.fit(train_images, train_labels, epochs=15, batch_size=64, validation_split=0.2)

# 6. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nFinal Test Accuracy: {test_acc*100:.2f}%")

# 7. Visualization: Loss Curves
# In a well-regularized model, Training Loss and Validation Loss should remain close.
plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Effect of Regularization: Training vs Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()