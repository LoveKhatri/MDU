import tensorflow as tf
from tensorflow.keras import layers, models, datasets, optimizers
import matplotlib.pyplot as plt

# 1. Load CIFAR-10 Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# 2. Preprocessing
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# One-hot encoding labels (10 classes)
train_labels = tf.keras.utils.to_categorical(train_labels, 10)
test_labels = tf.keras.utils.to_categorical(test_labels, 10)

# 3. Build "Mini-VGG" Architecture
# We use the VGG structure (Conv-Conv-Pool) but with fewer filters to save memory
model = models.Sequential()

# Block 1
model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Block 2
model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Block 3
model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Flatten and Dense Layers (The "Classifier" part)
model.add(layers.Flatten())

# Reduced from 4096 to 512 to prevent Memory Allocation Errors
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5)) 
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5))

# Output Layer
model.add(layers.Dense(10, activation='softmax'))

# 4. Compile the Model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Print summary to verify it fits in memory (Should be < 5 Million params now)
model.summary()

# 5. Train the Model
# We use a small batch size (32) to further ensure no memory crashes
print("\nTraining Optimized VGG on CIFAR-10...")
history = model.fit(train_images, train_labels, epochs=5, batch_size=32, validation_split=0.1)

# 6. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nVGG Test Accuracy: {test_acc*100:.2f}%")

# 7. Visualization
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('VGG Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()