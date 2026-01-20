import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 1. Load Dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# 2. Preprocessing
# One-hot encode the target variable (Species: 0, 1, 2 -> [1,0,0], [0,1,0], [0,0,1])
# Handle scikit-learn version differences: sparse_output (>=1.2) vs sparse (<1.2)
try:
    encoder = OneHotEncoder(sparse_output=False)
except TypeError:
    encoder = OneHotEncoder(sparse=False)
y_encoded = encoder.fit_transform(y)

# Split into Training (70%) and Test (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# 3. Build the Artificial Neural Network
model = Sequential()

# Input Layer & First Hidden Layer
# 4 input features, 10 neurons in hidden layer
model.add(Dense(10, input_shape=(4,), activation='relu', name='Hidden_Layer'))

# Output Layer
# 3 neurons (one for each class), Softmax for probability distribution
model.add(Dense(3, activation='softmax', name='Output_Layer'))

# 4. Compile the Model
# Optimizer: Adam (efficient variant of Gradient Descent/Backpropagation)
# Loss: Categorical Crossentropy (standard for multi-class classification)
model.compile(optimizer=Adam(learning_rate=0.01), 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 5. Train the Model
print("Training the model...")
history = model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

# 6. Evaluate the Model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\n" + "="*30)
print(f"Final Test Loss: {loss:.4f}")
print(f"Final Test Accuracy: {accuracy*100:.2f}%")
print("="*30)

# Optional: Predict on a single sample
sample_prediction = model.predict(X_test[:1])
print(f"\nPrediction for first test sample: {sample_prediction}")
print(f"Actual Class: {y_test[:1]}")