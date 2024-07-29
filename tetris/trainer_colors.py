import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from load_variants import variants  # Import the loaded variants

from colors import tetris_colors

# Unificar ambos diccionarios
combined_colors = {**tetris_colors, **variants}

# Preparar los datos
colors = np.array(list(combined_colors.keys()))
pieces = np.array(list(combined_colors.values()))

# Codificar las etiquetas de piezas
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(pieces)

# Convertir las etiquetas a una representación one-hot
one_hot_labels = np.eye(len(np.unique(integer_encoded)))[integer_encoded]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(colors, one_hot_labels, test_size=0.2, random_state=42)

# Definir la red neuronal
class TetrisNet(nn.Module):
    def __init__(self):
        super(TetrisNet, self).__init__()
        self.fc1 = nn.Linear(3, 64)
        self.dropout = nn.Dropout(0.5)  # Dropout con una probabilidad del 50%
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, len(np.unique(integer_encoded)))
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)  # Aplicar dropout
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Crear el modelo, definir la pérdida y el optimizador
model = TetrisNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenar el modelo
epochs = 5000
for epoch in range(epochs):
    model.train()
    inputs = torch.tensor(X_train, dtype=torch.float32)
    labels = torch.tensor(np.argmax(y_train, axis=1), dtype=torch.long)
    
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')

# Guardar el modelo y el label encoder
torch.save(model.state_dict(), 'tetris_model.pth')
np.save('label_encoder_classes.npy', label_encoder.classes_)
print("Modelo y label encoder guardados con éxito.")
