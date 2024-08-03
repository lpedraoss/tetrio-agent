import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Definir la red neuronal
class TetrisNet(nn.Module):
    def __init__(self):
        super(TetrisNet, self).__init__()
        self.fc1 = nn.Linear(3, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 8)  # Cambia el número 7 si hay más o menos clases
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Variables globales para el modelo y el label encoder
model = None
label_encoder = None

def load_models_torch():
    global model, label_encoder
    model = TetrisNet()
    model.load_state_dict(torch.load('tetris_model.pth', map_location=torch.device('cpu')))
    model.eval()
    label_encoder_classes = np.load('label_encoder_classes.npy', allow_pickle=True)
    label_encoder = LabelEncoder()
    label_encoder.classes_ = label_encoder_classes

def find_colors_tetris_piece(color):
    global model, label_encoder
    color_tensor = torch.tensor([color], dtype=torch.float32)
    output = model(color_tensor)
    predicted_piece = label_encoder.inverse_transform([torch.argmax(output).item()])
    return predicted_piece[0]
#load_models_torch()
#n = find_colors_tetris_piece((149,77,159))
#print('se ha predecido ==> ',n, 'se esperaba ==>','t')