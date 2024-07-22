import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class FoodDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

class NutritionalModel(nn.Module):
    def __init__(self):
        super(NutritionalModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def train_model(data, epochs=10, lr=0.001):
    dataset = FoodDataset(data)
    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

    model = NutritionalModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        for inputs in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs.float())
            loss = criterion(outputs, torch.zeros(outputs.size()))
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

    return model

if __name__ == "__main__":
    data = [torch.tensor([1.0] * 10) for _ in range(100)]  # Ejemplo de datos
    trained_model = train_model(data)
