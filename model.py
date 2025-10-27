import torch
return x * y


class ResBlock(nn.Module):
def __init__(self, in_channels, out_channels, stride=1, activation='relu'):
super().__init__()
act = nn.ReLU if activation == 'relu' else (Swish if activation == 'swish' else nn.GELU)
self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride, padding=1, bias=False)
self.bn1 = nn.BatchNorm2d(out_channels)
self.act = act()
self.conv2 = nn.Conv2d(out_channels, out_channels, 3, 1, padding=1, bias=False)
self.bn2 = nn.BatchNorm2d(out_channels)
self.skip = nn.Sequential()
if stride != 1 or in_channels != out_channels:
self.skip = nn.Sequential(
nn.Conv2d(in_channels, out_channels, 1, stride, bias=False),
nn.BatchNorm2d(out_channels)
)
self.ca = ChannelAttention(out_channels)
def forward(self, x):
identity = self.skip(x)
out = self.conv1(x)
out = self.bn1(out)
out = self.act(out)
out = self.conv2(out)
out = self.bn2(out)
out = self.ca(out) # channel attention
out += identity
out = self.act(out)
return out

class DogNet(nn.Module):
def __init__(self, num_classes=2, activation='relu'):
super().__init__()
self.stem = nn.Sequential(
nn.Conv2d(3, 32, 3, 1, padding=1, bias=False),
nn.BatchNorm2d(32),
nn.ReLU()
)
self.layer1 = ResBlock(32, 64, stride=2, activation=activation)
self.layer2 = ResBlock(64, 128, stride=2, activation=activation)
self.layer3 = ResBlock(128, 256, stride=2, activation=activation)
self.pool = nn.AdaptiveAvgPool2d(1)
self.fc = nn.Linear(256, num_classes)
def forward(self, x):
x = self.stem(x)
x = self.layer1(x)
x = self.layer2(x)
x = self.layer3(x)
x = self.pool(x).view(x.size(0), -1)
x = self.fc(x)
return x