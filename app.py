import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, callbacks
import hashlib
from collections import Counter
import streamlit as st

# Dictionary to store device hashes
device_hashes = {}

# Function to generate a SHA-256 hash for the given device label
def generate_hash(device_label):
    if device_label not in device_hashes:
        hashed_value = hashlib.sha256(str(device_label).encode()).hexdigest()
        device_hashes[device_label] = hashed_value
    return device_hashes[device_label]

# Function to read and preprocess data from a file
def read_and_preprocess_data(file_path, has_labels=True):
    X = []
    y = []
    encoding = 'utf-8-sig' if not has_labels else 'utf-8'  # Use 'utf-8-sig' for new_data if necessary
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            parts = line.strip().split(' ')
            features = np.array([int(bit) for bit in parts[0]], dtype=int)
            X.append(features)
            if has_labels and len(parts) > 1:
                y.append(int(parts[1]))
    X = np.array(X)
    if has_labels:
        y = np.array(y)
        num_classes = np.unique(y).size
        y_categorical = keras.utils.to_categorical(y - 1, num_classes=num_classes)
        return X, y_categorical, num_classes
    return X, None, None

# Function to create the model
def create_model(input_shape, num_classes, learning_rate, dropout_rate):
    model = keras.Sequential([
        keras.Input(shape=(input_shape,)),
        layers.Reshape((input_shape, 1)),  # Needed for Conv1D
        layers.Conv1D(32, kernel_size=3, activation='relu', padding='same'),
        layers.Dropout(dropout_rate),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def load_model_and_predict(X):
    model = keras.load()

# Training the model

#print("Training the model...")
#X_train, y_train_categorical, num_classes = read_and_preprocess_data('DoraHack/training_data.txt', has_labels=True)
#input_shape = X_train.shape[1]
#best_accuracy = 0
#best_params = {}


#learning_rates = [0.01, 0.001, 0.0001]  # Different learning rates to try
#dropout_rates = [0.3, 0.5, 0.7]  # Different dropout rates to try

#for lr in [0.01, 0.001, 0.0001]:
#    for dr in [0.3, 0.5, 0.7] :
#        model = create_model(input_shape, num_classes, lr, dr)
#        history = model.fit(X_train, y_train_categorical, epochs=10, validation_split=0.1, verbose=0)
#        val_accuracy = max(history.history['val_accuracy'])
#        if val_accuracy > best_accuracy:
#            best_accuracy = val_accuracy
#            best_params = {'learning_rate': lr, 'dropout_rate': dr}
#            model.save('best_model.h5')

# print("Best validation accuracy:", best_accuracy)
# print("Best parameters:", best_params)
    
def load_model_and_predict(X_new):
    model = tf.keras.models.load_model("bestmodel.h5")  # Replace "your_model_path.h5" with the path to your model file
    predictions = model.predict(X_new)
    # Assuming predictions are one-hot encoded, convert them to labels
    labels = np.argmax(predictions, axis=1)
    return labels

# Streamlit UI
st.title('Quantum Computing Predictions')
input_string = st.text_area("Enter a binary string (100 characters of 0s and 1s):", max_chars=100)

if st.button('Predict'):
    if len(input_string) != 100 or not set(input_string).issubset({'0', '1'}):
        st.error("Input must be exactly 100 characters long and contain only 0s and 1s.")
    else:
        X_new = np.array([[int(bit) for bit in input_string]], dtype=int)
        predicted_labels = load_model_and_predict(X_new)
        total_samples = len(predicted_labels)
        label_counts = Counter(predicted_labels)
        result_str = ""
        for label, count in label_counts.items():
            percentage = (count / total_samples) * 100
            hash_address = generate_hash(str(label))
            result_str += f"Label {label} appears {count} times ({percentage:.2f}%), Blockchain Address: {hash_address}\n"
        st.text(result_str)