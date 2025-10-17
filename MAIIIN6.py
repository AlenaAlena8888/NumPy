################import numpy as np
###############import pandas as pd
###########import matplotlib.pyplot as plt
#############from sklearn.model_selection import train_test_split
#############from sklearn.preprocessing import StandardScaler, LabelBinarizer
################from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
#########################import seaborn as sns

def load_letter_data():
    n_samples = 5000
    X = np.random.rand(n_samples, 28 * 28)
    y = np.random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), n_samples)
    return X, y

def preprocess_data(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    lb = LabelBinarizer()
    y_encoded = lb.fit_transform(y)
    return X_scaled, y_encoded, lb

def visualize_letters(X, y, samples=26):
    fig, axes = plt.subplots(4, 7, figsize=(14, 8))
    fig.suptitle("Приклади літер A-Z", fontsize=16)
    for i, ax in enumerate(axes.flatten()):
        if i >= samples:
            break
        img = X[i].reshape(28, 28)
        ax.imshow(img, cmap='gray')
        ax.set_title(y[i])
        ax.axis('off')
    plt.tight_layout()
    plt.show()

class LetterPerceptron:
    def __init__(self, input_size, hidden_size, output_size=26, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.lr = learning_rate

        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def softmax(self, x):
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e_x / e_x.sum(axis=1, keepdims=True)

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def compute_loss(self, y_true, y_pred):
        eps = 1e-15
        y_pred = np.clip(y_pred, eps, 1 - eps)
        return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))

    def backward(self, X, y_true, y_pred):
        m = X.shape[0]
        dz2 = (y_pred - y_true) / m
        dW2 = self.a1.T @ dz2
        db2 = np.sum(dz2, axis=0, keepdims=True)

        dz1 = dz2 @ self.W2.T * self.sigmoid_derivative(self.a1)
        dW1 = X.T @ dz1
        db1 = np.sum(dz1, axis=0, keepdims=True)

        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def train(self, X_train, y_train, X_val, y_val, epochs=100):
        history = {'loss': [], 'val_loss': []}
        for epoch in range(epochs):
            y_pred = self.forward(X_train)
            loss = self.compute_loss(y_train, y_pred)
            history['loss'].append(loss)

            y_val_pred = self.forward(X_val)
            val_loss = self.compute_loss(y_val, y_val_pred)
            history['val_loss'].append(val_loss)

            self.backward(X_train, y_train, y_pred)

            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs} - loss: {loss:.4f} - val_loss: {val_loss:.4f}")
        return history

    def predict(self, X):
        y_pred = self.forward(X)
        return np.argmax(y_pred, axis=1)

X, y = load_letter_data()
X_scaled, y_encoded, lb = preprocess_data(X, y)
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

visualize_letters(X, y)

model = LetterPerceptron(input_size=28 * 28, hidden_size=100, output_size=26, learning_rate=0.1)
history = model.train(X_train, y_train, X_val, y_val, epochs=100)

y_val_pred = model.predict(X_val)
y_val_true = np.argmax(y_val, axis=1)

print("Точність на валідації:", accuracy_score(y_val_true, y_val_pred))
print(classification_report(y_val_true, y_val_pred, target_names=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))

conf_matrix = confusion_matrix(y_val_true, y_val_pred)
plt.figure(figsize=(12, 10))
sns.heatmap(conf_matrix, annot=True, fmt="d", xticklabels=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            yticklabels=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), cmap="Blues")
plt.xlabel("Прогноз")
plt.ylabel("Істина")
plt.title("Матриця помилок")
plt.show()
