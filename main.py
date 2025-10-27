# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


import argparse


test_transform = transforms.Compose([
transforms.ToTensor(),
transforms.Normalize((0.4914, 0.4822, 0.4465), (0.247, 0.243, 0.261))
])


train_full = datasets.CIFAR10(root='./data', train=True, download=True)
test_full = datasets.CIFAR10(root='./data', train=False, download=True)

train_idx = [i for i, (_, y) in enumerate(train_full) if y == DOG_CLASS]
test_idx = [i for i, (_, y) in enumerate(test_full) if y == DOG_CLASS]

np.random.shuffle(train_idx)
np.random.shuffle(test_idx)


TRAIN_N = 3000
TEST_N = 600
train_idx = train_idx[:TRAIN_N]
test_idx = test_idx[:TEST_N]

class CIFARSubsetWithTransform(torch.utils.data.Dataset):
def __init__(self, dataset, indices, transform=None):
self.dataset = dataset
self.indices = indices
self.transform = transform
def __len__(self):
return len(self.indices)
def __getitem__(self, idx):
img, label = self.dataset[self.indices[idx]]
if self.transform:
img = self.transform(img)
return img, 1


train_ds = CIFARSubsetWithTransform(train_full, train_idx, transform=train_transform)
test_dogs = CIFARSubsetWithTransform(test_full, test_idx, transform=test_transform)
non_dog_idx = [i for i, (_, y) in enumerate(test_full) if y != DOG_CLASS]
np.random.shuffle(non_dog_idx)
non_dog_idx = non_dog_idx[:TEST_N]

class CIFARSubsetMixed(torch.utils.data.Dataset):
def __init__(self, dataset, dog_indices, non_dog_indices, transform=None):
self.dataset = dataset
self.dog_indices = dog_indices
self.non_dog_indices = non_dog_indices