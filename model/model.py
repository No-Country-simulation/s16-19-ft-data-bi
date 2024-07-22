import torch.nn as nn
import torch

class NutritionalModel(nn.Module):
    def __init__(self):
        super(NutritionalModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
