import torch
import torch.nn.functional as F
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
import random

def label_smoothing_loss(pred, target, smoothing=0.1):
# pred: logits, target: long
n_class = pred.size(1)
with torch.no_grad():
true_dist = torch.zeros_like(pred)
true_dist.fill_(smoothing / (n_class - 1))
true_dist.scatter_(1, target.data.unsqueeze(1), 1.0 - smoothing)
return torch.mean(torch.sum(-true_dist * F.log_softmax(pred, dim=1), dim=1))

def mixup_data(x, y, alpha=0.4):
if alpha <= 0:
return x, y, None, None, 1.0
lam = np.random.beta(alpha, alpha)
batch_size = x.size()[0]
index = torch.randperm(batch_size)
mixed_x = lam * x + (1 - lam) * x[index, :]
y_a, y_b = y, y[index]
return mixed_x, y_a, y_b, index, lam


def mixup_criterion(criterion, pred, y_a, y_b, lam):
return lam * criterion(pred, y_a) + (1 - lam) * criterion(pred, y_b)


def accuracy(preds, targets):
_, p = preds.max(1)
return (p == targets).float().mean().item()


def set_seed(seed=42):
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)