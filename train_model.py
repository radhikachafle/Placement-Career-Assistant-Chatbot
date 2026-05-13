import os
import sys
import pickle
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from training.preprocess import preprocess
from sklearn.neural_network import MLPClassifier

os.makedirs("model", exist_ok=True)


def train():
    print("Starting ANN training...")

    X_train, y_train, words, classes = preprocess()

    y_labels = np.argmax(y_train, axis=1)

    model = MLPClassifier(
        hidden_layer_sizes=(128, 64),
        activation='relu',
        solver='adam',
        max_iter=500,
        random_state=42,
        verbose=True
    )

    model.fit(X_train, y_labels)

    pickle.dump(model, open('model/chatbot_model.pkl', 'wb'))
    print("Training complete! Model saved to model/chatbot_model.pkl")


if __name__ == "__main__":
    train()