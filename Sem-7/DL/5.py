import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

# 1. Load the MNIST Dataset
# MNIST contains 60,000 training images and 10,000 testing images of handwritten digits (0-9)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. Preprocessing
# Normalize pixel values to be between 0 and 1
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# 3. Build the Deep Feed Forward Network
model = Sequential()

# Input Layer: Flattens the 28x28 image into a 784 vector
model.add(Flatten(input_shape=(28, 28)))

# Hidden Layer 1
model.add(Dense(128, activation='relu'))

# Hidden Layer 2
model.add(Dense(64, activation='relu'))

# Output Layer: 10 neurons for the 10 digit classes
model.add(Dense(10, activation='softmax'))

# 4. Compile the Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train the Model
print("Starting training...")
history = model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# 6. Evaluate on Test Data
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

print("\n" + "="*30)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc*100:.2f}%")
print("="*30)

# 7. Visualization of Predictions
# Predict classes for the test set
predictions = model.predict(X_test)

# Plot the first 5 test images with their predicted labels
plt.figure(figsize=(10, 4))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_test[i], cmap='gray')
    predicted_label = np.argmax(predictions[i])
    true_label = y_test[i]
    plt.title(f"Pred: {predicted_label}\nTrue: {true_label}")
    plt.axis('off')

plt.tight_layout()
plt.show()