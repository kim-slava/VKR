import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# Предполагается, что у вас есть собственный датасет, который вы хотите использовать.
# Для этого примера мы создадим класс Dataset.

class CustomDataset(Dataset):
    def __init__(self, data_path, transform=None):
        # Инициализируем датасет
        self.data = ...  # Загрузите данные из вашего датасета, например, изображения
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        if self.transform:
            sample = self.transform(sample)
        return sample

# Предположим, что у вас есть класс Autoencoder, который определяет архитектуру вашего автоэнкодера.

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 3, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Теперь мы определяем функцию обучения.

def train_autoencoder(autoencoder, train_loader, criterion, optimizer, num_epochs=10):
    for epoch in range(num_epochs):
        running_loss = 0.0
        for data in train_loader:
            inputs = data
            optimizer.zero_grad()
            outputs = autoencoder(inputs)
            loss = criterion(outputs, inputs)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch {epoch+1}, Loss: {running_loss / len(train_loader)}")

# Теперь создаем экземпляры нашего датасета и модели, и задаем параметры обучения.

transform = transforms.Compose([
    transforms.ToTensor()
])

dataset = CustomDataset(data_path='path/to/your/dataset', transform=transform)
train_loader = DataLoader(dataset, batch_size=64, shuffle=True)

autoencoder = Autoencoder()
criterion = nn.MSELoss()
optimizer = optim.Adam(autoencoder.parameters(), lr=0.001)

# Обучаем автоэнкодер

train_autoencoder(autoencoder, train_loader, criterion, optimizer, num_epochs=10)

