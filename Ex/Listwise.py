import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import OneHotEncoder

# Load data
df = pd.read_csv("ranking_data.csv")
X_raw = df[["mau", "chieu_dai", "loai"]]
y = df["relevance"].values

# Encode
enc = OneHotEncoder()
X = enc.fit_transform(X_raw).toarray()

# Định nghĩa model
class RankNet(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, 1)
    def forward(self, x):
        return self.fc(x)

model = RankNet(X.shape[1])
optimizer = optim.Adam(model.parameters(), lr=0.05)

def listnet_loss(pred, true):
    P_true = torch.softmax(true, dim=0)
    P_pred = torch.log_softmax(pred, dim=0)
    return -(P_true * P_pred).sum()

X_t = torch.tensor(X, dtype=torch.float32)
y_t = torch.tensor(y, dtype=torch.float32)

# Train
for epoch in range(100):
    optimizer.zero_grad()
    scores = model(X_t).squeeze()
    loss = listnet_loss(scores, y_t)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f"Epoch {epoch}, Loss={loss.item():.4f}")

print("=== Listwise ===")
scores = model(X_t).detach().numpy().squeeze()
ranking = scores.argsort()[::-1]
print("Thứ hạng dự đoán (top 10):", ranking[:10])
print("Điểm relevance thực tế (top 10 theo dự đoán):", y[ranking[:10]])