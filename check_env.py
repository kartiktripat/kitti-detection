import torch
import torchvision
import torchmetrics

print("torch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("torchmetrics:", torchmetrics.__version__)
print("MPS available:", torch.backends.mps.is_available())
